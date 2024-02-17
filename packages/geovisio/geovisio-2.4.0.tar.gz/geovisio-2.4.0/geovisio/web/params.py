from uuid import UUID
from geovisio import errors
import dateutil.parser
from dateutil import tz
from dateutil.parser import parse as dateparser
import datetime
import re
from werkzeug.datastructures import MultiDict
from dataclasses import dataclass, field
from typing import Optional, Tuple, Dict, List, Any
from pygeofilter.backends.sql import to_sql_where
from pygeofilter.parsers.ecql import parse as ecql_parser
from psycopg import sql
from geovisio.utils.sequences import FieldMapping, SortBy, SortByField, STAC_FIELD_MAPPINGS, STAC_FIELD_TO_SQL_FILTER, SQLDirection


RGX_SORTBY = re.compile("[+-]?[A-Za-z_].*(,[+-]?[A-Za-z_].*)*")
SEQUENCES_DEFAULT_FETCH = 100
SEQUENCES_MAX_FETCH = 1000


def parse_datetime(value, error, fallback_as_UTC=False):
    """
    Parse a datetime and raises an error if the parse fails
    Note: if fallback_as_UTC is True and the date as no parsed timezone, consider it as UTC
    This should be done for server's date (like a date automaticaly set by the server) but not user's date (like the datetime of the picture)

    >>> parse_datetime("2023-06-17T21:22:18.406856+02:00", error="")
    datetime.datetime(2023, 6, 17, 21, 22, 18, 406856, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))
    >>> parse_datetime("2020-05-31", error="")
    datetime.datetime(2020, 5, 31, 0, 0)
    >>> parse_datetime("20231", error="oh no") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: oh no
    >>> parse_datetime("2020-05-31T10:00:00", error="")
    datetime.datetime(2020, 5, 31, 10, 0)
    >>> parse_datetime("2020-05-31T10:00:00", error="", fallback_as_UTC=True) ==  parse_datetime("2020-05-31T10:00:00", error="").astimezone(tz.UTC)
    True

    """
    # Hack to parse a date
    # dateutils know how to parse lots of date, but fail to correctly parse date formated by `datetime.isoformat()`
    # (like all the dates returned by the API).
    # datetime.isoformat is like: `2023-06-17T21:22:18.406856+02:00`
    # dateutils silently fails the parse, and create an incorect date
    # so we first try to parse it like an isoformated date, and if this fails we try the flexible dateutils
    d = None
    try:
        d = datetime.datetime.fromisoformat(value)
    except ValueError as e:
        pass
    if not d:
        try:
            d = dateparser(value)
            if value.endswith("Z"):
                # dateparser sometimes does not recognize the trailing 'Z' as utc
                fallback_as_UTC = True
        except dateutil.parser.ParserError as e:
            raise errors.InvalidAPIUsage(message=error, payload={"details": {"error": str(e)}}, status_code=400)
    if fallback_as_UTC and (d.tzinfo is None or d.tzinfo == tz.tzlocal()):
        d = d.astimezone(tz.UTC)
    return d


def parse_datetime_interval(value: Optional[str]) -> Tuple[Optional[datetime.datetime], Optional[datetime.datetime]]:
    """Reads a STAC datetime interval query parameter
    Can either be a closed interval, or an open one.

    `None` on an end of the interval means no bound.

    >>> parse_datetime_interval(None)
    (None, None)

    >>> parse_datetime_interval("2018-02-12T00:00:00+00:00/..")
    (datetime.datetime(2018, 2, 12, 0, 0, tzinfo=datetime.timezone.utc), None)

    >>> parse_datetime_interval("../2018-03-18T12:31:12+00:00")
    (None, datetime.datetime(2018, 3, 18, 12, 31, 12, tzinfo=datetime.timezone.utc))"""
    if value is None:
        return (None, None)
    dates = value.split("/")

    if len(dates) == 1:
        d = parse_datetime(dates[0], error=f"Invalid `datetime` argument", fallback_as_UTC=True)
        return (d, d)

    elif len(dates) == 2:
        # Check if interval is closed or open-ended
        mind, maxd = dates
        mind = None if mind == ".." else parse_datetime(mind, error=f"Invalid start date in `datetime` argument", fallback_as_UTC=True)
        maxd = None if maxd == ".." else parse_datetime(maxd, error=f"Invalid end date in `datetime` argument", fallback_as_UTC=True)
        return (mind, maxd)
    else:
        raise errors.InvalidAPIUsage("Parameter datetime should contain one or two dates", status_code=400)


def parse_bbox(value: Optional[Any], tryFallbacks=True):
    """Reads a STAC bbox query parameter
    >>> parse_bbox("0,0,1,1")
    [0.0, 0.0, 1.0, 1.0]
    >>> parse_bbox("-1.5,-2.5,4.78,2.21")
    [-1.5, -2.5, 4.78, 2.21]
    >>> parse_bbox(None)

    >>> parse_bbox("-181,0,-10,0.1") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Parameter bbox must contain valid longitude (-180 to 180) and latitude (-90 to 90) values
    >>> parse_bbox("0,-91,0.1,0") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Parameter bbox must contain valid longitude (-180 to 180) and latitude (-90 to 90) values
    >>> parse_bbox("[-1.5,-2.5,4.78,2.21]")
    [-1.5, -2.5, 4.78, 2.21]
    >>> parse_bbox([-1.5,-2.5,4.78,2.21])
    [-1.5, -2.5, 4.78, 2.21]
    >>> parse_bbox(["[-1.5,-2.5,4.78,2.21]"])
    [-1.5, -2.5, 4.78, 2.21]
    >>> parse_bbox([])

    >>> parse_bbox([1,2,3]) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Parameter bbox must be in format [minX, minY, maxX, maxY]
    >>> parse_bbox(MultiDict([('bbox', 0), ('bbox', -15), ('bbox', 15.7), ('bbox', '-13.8')]))
    [0.0, -15.0, 15.7, -13.8]
    >>> parse_bbox(MultiDict([('bbox', [0.0, -15.0, 15.7, -13.8])]))
    [0.0, -15.0, 15.7, -13.8]
    >>> parse_bbox(MultiDict([('bbox', '[0.0, -15.0, 15.7, -13.8]')]))
    [0.0, -15.0, 15.7, -13.8]
    """

    if value is not None:
        try:
            if isinstance(value, MultiDict):
                v = value.getlist("bbox")
                if len(v) == 1:
                    value = v[0]
                else:
                    value = v

            if isinstance(value, list):
                if len(value) == 1 and tryFallbacks:
                    return parse_bbox(value[0], False)
                bbox = [float(n) for n in value]
            elif isinstance(value, str):
                value = value.replace("[", "").replace("]", "")
                bbox = [float(n) for n in value.split(",")]
            else:
                raise ValueError()

            if len(bbox) == 0:
                return None
            if len(bbox) != 4 or not all(isinstance(x, float) for x in bbox):
                raise ValueError()
            elif (
                bbox[0] < -180
                or bbox[0] > 180
                or bbox[1] < -90
                or bbox[1] > 90
                or bbox[2] < -180
                or bbox[2] > 180
                or bbox[3] < -90
                or bbox[3] > 90
            ):
                raise errors.InvalidAPIUsage(
                    "Parameter bbox must contain valid longitude (-180 to 180) and latitude (-90 to 90) values", status_code=400
                )
            else:
                return bbox
        except ValueError:
            raise errors.InvalidAPIUsage("Parameter bbox must be in format [minX, minY, maxX, maxY]", status_code=400)
    else:
        return None


def parse_list(value: Optional[Any], tryFallbacks: bool = True, paramName: Optional[str] = None):
    """Reads STAC query parameters that are structured like lists.

    >>> parse_list('a')
    ['a']
    >>> parse_list('0,0,1,1')
    ['0', '0', '1', '1']
    >>> parse_list('-1.5,-2.5,4.78,2.21')
    ['-1.5', '-2.5', '4.78', '2.21']
    >>> parse_list(None)

    >>> parse_list('[-1.5,-2.5,4.78,2.21]')
    ['-1.5', '-2.5', '4.78', '2.21']
    >>> parse_list(['a', 'b', 'c', 'd'])
    ['a', 'b', 'c', 'd']
    >>> parse_list(['[-1.5,-2.5,4.78,2.21]'])
    ['-1.5', '-2.5', '4.78', '2.21']
    >>> parse_list('["a", "b"]')
    ['a', 'b']
    >>> parse_list("['a', 'b']")
    ['a', 'b']
    >>> parse_list([])

    >>> parse_list(MultiDict([('collections', 'a'), ('collections', 'b')]))

    >>> parse_list(MultiDict([('collections', 'a'), ('collections', 'b')]), paramName = 'collections')
    ['a', 'b']
    >>> parse_list(MultiDict([('collections', ['a', 'b', 'c', 'd'])]), paramName = 'collections')
    ['a', 'b', 'c', 'd']
    >>> parse_list(MultiDict([('collections', '[a, b, c, d]')]), paramName = 'collections')
    ['a', 'b', 'c', 'd']
    >>> parse_list(MultiDict([('collections', '["a", "b", "c", "d"]')]), paramName = 'collections')
    ['a', 'b', 'c', 'd']
    >>> parse_list(MultiDict([('collections', "['a', 'b', 'c', 'd']")]), paramName = 'collections')
    ['a', 'b', 'c', 'd']
    >>> parse_list(42, paramName = 'test') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Parameter test must be a valid list
    >>> parse_list(42) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Parameter must be a valid list
    """

    if value is not None:
        if isinstance(value, MultiDict):
            v = value.getlist(paramName)
            if len(v) == 1:
                value = v[0]
            else:
                value = v

        if isinstance(value, list):
            if len(value) == 1 and tryFallbacks:
                return parse_list(value[0], False, paramName)
            res = value
        elif isinstance(value, str):
            value = value.replace("[", "").replace("]", "")
            res = [n.strip() for n in value.split(",")]
        else:
            raise errors.InvalidAPIUsage(f"Parameter {paramName or ''} must be a valid list", status_code=400)

        if len(res) == 0:
            return None
        else:
            return [n.strip('"').strip("'") for n in res]

    else:
        return None


def parse_filter(value: Optional[str]) -> Optional[sql.SQL]:
    """Reads STAC filter parameter and sends SQL condition back.

    >>> parse_filter('')

    >>> parse_filter("updated >= '2023-12-31'")
    SQL("(s.updated_at >= '2023-12-31')")
    >>> parse_filter("updated >= '2023-12-31' AND created < '2023-10-31'")
    SQL("((s.updated_at >= '2023-12-31') AND (s.inserted_at < '2023-10-31'))")
    >>> parse_filter("status IN ('deleted','ready')")
    SQL("s.status IN ('deleted', 'ready')")
    >>> parse_filter("status = 'deleted' OR status = 'ready'")
    SQL("((s.status = 'deleted') OR (s.status = 'ready'))")
    >>> parse_filter('invalid = 10') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Unsupported filter parameter
    >>> parse_filter('updated == 10') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Unsupported filter parameter
    """
    if value is not None and len(value) > 0:
        try:
            filterAst = ecql_parser(value)
            f = to_sql_where(filterAst, STAC_FIELD_TO_SQL_FILTER).replace('"', "")
            return sql.SQL(f)
        except:
            raise errors.InvalidAPIUsage(f"Unsupported filter parameter", status_code=400)
    else:
        return None


def parse_sortby(value: Optional[str]) -> Optional[SortBy]:
    """Reads STAC/OGC sortby parameter, and sends a SQL ORDER BY string.

    Parameters
    ----------
    value : str
        The HTTP query parameter value to read (example: "+nb,-created")
    variableMappings : dict
        Mapping of names between HTTP query parameter and database fields

    Returns
    -------
    Tuple(SQL ORDER BY string, first SQL column name, first SQL order direction ASC/DESC)

    None if no sort by is found

    >>> parse_sortby(None)
    >>> parse_sortby("")
    >>> parse_sortby('updated')
    SortBy(fields=[SortByField(field=FieldMapping(sql_column=SQL('updated_at'), stac='updated'), direction=<SQLDirection.ASC: SQL('ASC')>)])
    >>> parse_sortby('+created')
    SortBy(fields=[SortByField(field=FieldMapping(sql_column=SQL('inserted_at'), stac='created'), direction=<SQLDirection.ASC: SQL('ASC')>)])
    >>> parse_sortby('-created')
    SortBy(fields=[SortByField(field=FieldMapping(sql_column=SQL('inserted_at'), stac='created'), direction=<SQLDirection.DESC: SQL('DESC')>)])
    >>> parse_sortby('+updated,-created')
    SortBy(fields=[SortByField(field=FieldMapping(sql_column=SQL('updated_at'), stac='updated'), direction=<SQLDirection.ASC: SQL('ASC')>), SortByField(field=FieldMapping(sql_column=SQL('inserted_at'), stac='created'), direction=<SQLDirection.DESC: SQL('DESC')>)])
    >>> parse_sortby('invalid') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Unsupported sortby parameter
    >>> parse_sortby('~nb') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: Unsupported sortby parameter
    """

    if value is not None and len(value) > 0:
        # Check value pattern
        if RGX_SORTBY.match(value):
            values = value.split(",")
            orders = []
            for v in values:
                direction = SQLDirection.DESC if v.startswith("-") else SQLDirection.ASC
                vOnly = v.replace("+", "").replace("-", "")

                # Check if in value mapping
                if vOnly not in STAC_FIELD_MAPPINGS:
                    raise errors.InvalidAPIUsage(f"Unsupported sortby parameter: invalid column name", status_code=400)
                field_mapping = STAC_FIELD_MAPPINGS[vOnly]

                orders.append(SortByField(field=field_mapping, direction=direction))

            # Create definitive ORDER string
            return SortBy(fields=orders)
        else:
            raise errors.InvalidAPIUsage(f"Unsupported sortby parameter: syntax isn't correct", status_code=400)
    else:
        return None


def parse_collections_limit(limit: Optional[str]) -> int:
    """Checks if given limit parameter is valid

    >>> parse_collections_limit('')
    100
    >>> parse_collections_limit('50')
    50
    >>> parse_collections_limit('9999999999') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: limit parameter should be an integer between 1 and 100
    >>> parse_collections_limit('prout') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    geovisio.errors.InvalidAPIUsage: limit parameter should be a valid, positive integer (between 1 and 100)
    """

    if limit is None or limit == "":
        return SEQUENCES_DEFAULT_FETCH

    try:
        int_limit = int(limit)
    except ValueError:
        raise errors.InvalidAPIUsage(f"limit parameter should be a valid, positive integer (between 1 and {SEQUENCES_MAX_FETCH})")

    if int_limit < 1 or int_limit > SEQUENCES_MAX_FETCH:
        raise errors.InvalidAPIUsage(f"limit parameter should be an integer between 1 and {SEQUENCES_MAX_FETCH}")
    else:
        return int_limit


def as_longitude(value: str, error):
    try:
        l = float(value)
    except ValueError as e:
        raise errors.InvalidAPIUsage(message=error, payload={"details": {"error": str(e)}})
    if l < -180 or l > 180:
        raise errors.InvalidAPIUsage(message=error, payload={"details": {"error": "longitude needs to be between -180 and 180"}})
    return l


def as_latitude(value: str, error):
    try:
        l = float(value)
    except ValueError as e:
        raise errors.InvalidAPIUsage(message=error, payload={"details": {"error": str(e)}})
    if l < -90 or l > 90:
        raise errors.InvalidAPIUsage(message=error, payload={"details": {"error": "latitude needs to be between -90 and 90"}})
    return l


def as_uuid(value: str, error: str) -> UUID:
    """Convert the value to an UUID and raises an error if it's not possible"""
    try:
        return UUID(value)
    except ValueError:
        raise errors.InvalidAPIUsage(error)

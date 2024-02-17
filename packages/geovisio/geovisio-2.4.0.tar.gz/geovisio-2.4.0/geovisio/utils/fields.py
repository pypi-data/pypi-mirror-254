from enum import Enum
from dataclasses import dataclass, field
from typing import Any, List, Dict, Optional, Generic, TypeVar, Protocol
from psycopg import sql


@dataclass
class FieldMapping:
    """Represent the mapping between a STAC field and a column in the database"""

    sql_column: sql.SQL
    stac: str

    @property
    def sql_filter(self) -> sql.Composable:
        return sql.SQL("s.{}").format(self.sql_column)


class SQLDirection(Enum):
    """Represent the direction in a SQL ORDER BY query"""

    ASC = sql.SQL("ASC")
    DESC = sql.SQL("DESC")


@dataclass
class SortByField:
    field: FieldMapping
    direction: SQLDirection

    def as_sql(self) -> sql.Composable:
        # Note: the column is the stac name, as the real sql column name will be aliased with the stac name in the query
        col = sql.SQL(self.field.stac)  # type: ignore
        return sql.SQL("{column} {dir}").format(column=col, dir=self.direction.value)

    def revert(self) -> sql.Composable:
        col = sql.SQL(self.field.stac)  # type: ignore
        revert_dir = SQLDirection.ASC if self.direction == SQLDirection.DESC else SQLDirection.DESC
        return sql.SQL("{column} {dir}").format(column=col, dir=revert_dir.value)


@dataclass
class SortBy:
    fields: List[SortByField] = field(default_factory=lambda: [])

    def as_sql(self) -> sql.Composable:
        return sql.SQL(", ").join([f.as_sql() for f in self.fields])

    def revert(self) -> sql.Composable:
        return sql.SQL(", ").join([f.revert() for f in self.fields])


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    def __lt__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


@dataclass
class Bounds(Generic[T]):
    """Represent some bounds (min and max) over a generic type"""

    min: T
    max: T

    def update(self, val: T):
        """Update the bounds if val is out of them"""
        self.min = min(self.min, val)
        self.max = max(self.max, val)


@dataclass
class BBox:
    """Represent a bounding box defined as 2 points"""

    minx: float
    maxx: float
    miny: float
    maxy: float

# Developing on the server

You want to work on GeoVisio and offer bug fixes or new features ? That's awesome ! 🤩

Here are some inputs about working with GeoVisio API code.

If something seems missing or incomplete, don't hesitate to contact us by [email](panieravide@riseup.net) or using [an issue](https://gitlab.com/geovisio/api/-/issues). We really want GeoVisio to be a collaborative project, so everyone is welcome (see our [code of conduct](../CODE_OF_CONDUCT.md)).

__Contents__

[[_TOC_]]


## Testing

We're trying to make GeoVisio as reliable and secure as possible. To ensure this, we rely heavily on code testing.

### Unit tests (Pytest)

Unit tests ensure that small parts of code are working as expected. We use the Pytest solution to run unit tests.

You can run tests by following these steps:

- In an environment variable, or a [test.env dot file](https://flask.palletsprojects.com/en/2.2.x/cli/?highlight=dotenv#environment-variables-from-dotenv), add a `DB_URL` parameter, which follows the `DB_URL` [parameter format](./11_Server_settings.md), so you can use a dedicated database for testing
- Run `pytest` command

Unit tests are available mainly in `/tests/` folder, some simpler tests are directly written as [doctests](https://docs.python.org/3/library/doctest.html) in their respective source files (in `/geovisio`).

If you're working on bug fixes or new features, please __make sure to add appropriate tests__ to keep GeoVisio level of quality.

Note that tests can be run using Docker with following commands:

```bash
# All tests (including heavy ones)
docker-compose \
	run --rm --build \
	-e DB_URL="postgres://gvs:gvspwd@db/geovisio" \
	backend test  # Replace test by test-ci for only running lighter tests
```

Also note that Pytest tests folders are cleaned-up after execution, temporary files only exist during test running time.

### STAC API conformance

Third-party tool [STAC API Validator](https://github.com/stac-utils/stac-api-validator) is used to ensure that GeoVisio API is compatible with [STAC API specifications](https://github.com/radiantearth/stac-api-spec). It is run automatically on our Gitlab CI, but can also be run manually with the following commands:

```bash
./tests/test_api_conformance.sh
```

## Code format

Before opening a pull requests, code need to be formated with [black](https://black.readthedocs.io).

Install development dependencies:
```bash
pip install -e .[dev]
```

Format sources:
```bash
black .
```

You can also install git [pre-commit](https://pre-commit.com/) hooks to format code on commit with:

```bash
pre-commit install
```

## Database

### Adding a new migration

To create a new migration, use [yoyo-migrations](https://ollycope.com/software/yoyo/latest/).

The `yoyo` binary should be available if the Python dependencies are installed.

The prefered way to create migration is to use raw SQL, but if needed a Python migration script can be added.

```bash
yoyo new -m "<a migration name>" --sql
```

(remove the `--sql` to generate a Python migration).

This will open an editor to a migration in `./migrations`.

Once saved, for SQL migrations, always provide another file named like the initial migration but with a `.rollback.sql` suffix, with the associated rollback actions.

Note: each migration is run inside a transaction.

#### Updating large tables

When performing a migration that update a potentially large table (like `pictures` or `pictures_sequence`, that can contains tens of millions rows), we don't want to lock the whole table for too long since it would cause downtime on the instance.

So when possible, the migration of a column should be written in batch (and as a best effort, the code should work on the updated or non updated table if possible).

The migration of pictures table can for example be written like:

```sql
CREATE OR REPLACE PROCEDURE update_all_pictures_with_important_stuff() AS
$$
DECLARE
   last_inserted_at TIMESTAMPTZ;
BEGIN
	SELECT min(inserted_at) - INTERVAL '1 minute' FROM pictures INTO last_inserted_at;

       WHILE last_inserted_at IS NOT NULL LOOP
		
		-- Temporary removal of all update triggers that needs to be removed, be sure to check all the update trigger, and see which should be deactivated
		DROP TRIGGER pictures_update_sequences_trg ON pictures;
		DROP TRIGGER pictures_updates_on_sequences_trg ON pictures;

		WITH 
			-- get a batch of 100 000 pictures to update
			pic_to_update AS (
				SELECT id, inserted_at from pictures where inserted_at > last_inserted_at ORDER BY inserted_at ASC LIMIT 100000
			)
			, updated_pic AS (
				UPDATE pictures 
					SET important_stuff = 'very_important' -- do real update here
					WHERE id in (SELECT id FROM pic_to_update)
			)
			SELECT MAX(inserted_at) FROM pic_to_update INTO last_inserted_at;
		
       RAISE NOTICE 'max insertion date is now %', last_inserted_at;


		-- Restore all deactivated triggers
		CREATE TRIGGER pictures_updates_on_sequences_trg
		AFTER UPDATE ON pictures
		REFERENCING NEW TABLE AS pictures_after
		FOR EACH STATEMENT
		EXECUTE FUNCTION pictures_updates_on_sequences();

		CREATE TRIGGER pictures_update_sequences_trg
		AFTER UPDATE ON pictures
		REFERENCING OLD TABLE AS old_table NEW TABLE AS new_table
		FOR EACH STATEMENT EXECUTE FUNCTION pictures_update_sequence();

        -- commit transaction (as a procedure is in an implicit transaction, it will start a new transaction after this)
		COMMIT;
   END LOOP;
   RAISE NOTICE 'update finished';
END
$$  LANGUAGE plpgsql;

CALL update_all_pictures_with_important_stuff();
DROP PROCEDURE update_all_pictures_with_important_stuff;

```

The migrations [`pictures-exiv2`](../migrations/20231018_01_4G3YE-pictures-exiv2.sql) and [`jobs-error`](../migrations/20231110_01_3p070-jobs-error.sql) are real case examples of this.

### Updating an instance database schema

Migrations are technically handled by [yoyo-migrations](https://ollycope.com/software/yoyo/latest/).

For advanced schema handling (like listing the migrations, replaying a migration, ...) you can use all yoyo's command.

For example, you can list all the migrations:

```bash
yoyo list --database postgresql+psycopg://user:pwd@host:port/database
```

Note: the database connection string should use `postgresql+psycopg://` in order to force yoyo to use Psycopg v3.

## Keycloak

To work on authentication functionalities, you might need a locally deployed Keycloak server.

To spawn a configured Keycloak, run:

```bash
docker-compose -f docker/docker-compose-keycloak.yml up
```

And wait for Keycloak to start.

:warning: beware that the configuration is not meant to be used in production!

Then provided the following variables to your local geovisio (either in a custom `.env` file or directly as environment variables, as stated in the [corresponding documentation section](./11_Server_settings.md)).

```.env
OAUTH_PROVIDER='oidc'
FLASK_SECRET_KEY='some secret key'
OAUTH_OIDC_URL='http://localhost:3030/realms/geovisio'
OAUTH_CLIENT_ID="geovisio"
OAUTH_CLIENT_SECRET="what_a_secret"
```

## Make a release

See [dedicated documentation](./90_Releases.md).

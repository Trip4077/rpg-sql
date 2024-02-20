from sqlite_example import connect_to_db, execute_query
from pg_helper import connect_to_pg, modify_pg
from queries import (
    SELECT_CHARACTERS,
    DROP_CHARACTER_TABLE,
    CREATE_CHARACTER_TABLE,
    insert_new_character
)

DB_NAME = 'yfzmkhac'
USER_NAME = 'yfzmkhac'
HOST_NAME = 'jelani.db.elephantsql.com'
PASSWORD = 'zVgeJ4rSgilcPjpAxbvTu_fZWfGglK8H'


if __name__ == '__main__':
    # Get SQLite3 data and connection
    sqlite_conn = connect_to_db()
    sqlite_characters = execute_query(sqlite_conn, SELECT_CHARACTERS)

    # Connect to PostgreSQL database and create fresh table
    pg_conn, pg_cursor = connect_to_pg(DB_NAME, USER_NAME, PASSWORD, HOST_NAME)

    modify_pg(pg_conn, pg_cursor, DROP_CHARACTER_TABLE)
    modify_pg(pg_conn, pg_cursor, CREATE_CHARACTER_TABLE)

    # Migrate Data
    for character in sqlite_characters:
        modify_pg(
            pg_conn, pg_cursor,
            insert_new_character(
                character[1], character[2], character[3], character[4],
                character[5], character[6], character[7], character[8]
            )
        )

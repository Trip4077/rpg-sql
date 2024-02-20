from sqlite_example import execute_query
from pg_helper import connect_to_pg, modify_pg
from pandas_helper import create_and_populate_sqlite
from queries import (
    SELECT_ALL_TITANIC_DATA,
    CREATE_TITANIC_TABLE,
    DROP_TITANIC_TABLE,
    insert_titanic_passenger
)

DB_NAME = 'fvqbnsjx'
USER_NAME = 'fvqbnsjx'
HOST_NAME = 'jelani.db.elephantsql.com'
PASSWORD = 'EsCx6Ar_O163G7ho46ymEn8t5ALXckle'

if __name__ == '__main__':
    # read in csv file
    # convert from csv to sqlite3
    sqlite_conn = create_and_populate_sqlite(
        "Titanic-Dataset.csv",
        "titanic.sqlite3",
        "titanic"
    )

    # fetch sqlite3 data
    titanic_data = execute_query(sqlite_conn, SELECT_ALL_TITANIC_DATA)

    # create pg connection
    pg_conn, pg_cursor = connect_to_pg(DB_NAME, USER_NAME, PASSWORD, HOST_NAME)

    # Create Fresh Table
    modify_pg(pg_conn, pg_cursor, DROP_TITANIC_TABLE)
    modify_pg(pg_conn, pg_cursor, CREATE_TITANIC_TABLE)

    # populate pg database with sqlite3 data
    for passenger in titanic_data:
        print(passenger[2])
        modify_pg(
            pg_conn, pg_cursor,
            insert_titanic_passenger(
                passenger[2], passenger[3], passenger[4], passenger[5],
                passenger[6], passenger[7], passenger[8], passenger[9],
                passenger[10], passenger[11], passenger[12]
            )
        )

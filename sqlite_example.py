import sqlite3
import queries as q


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(conn, query):
    curs = conn.cursor()

    return curs.execute(query).fetchall()


if __name__ == "__main__":
    connection = connect_to_db()

    results = execute_query(connection, q.AVG_CHARACTER_WEAPONS)

import psycopg2


def connect_to_pg(dbname, user, password, host):
    pg_conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host
    )

    pg_cursor = pg_conn.cursor()

    return pg_conn, pg_cursor


def modify_pg(conn, cursor, query):
    cursor.execute(query)
    conn.commit()


def fetch_data(cursor, query):
    cursor.execute(query)

    result = cursor.fetchall()

    return result

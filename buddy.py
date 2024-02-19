import pandas as pd
from sqlite_example import connect_to_db, execute_query
from queries import TOTAL_COUNT, NUM_100_OR_MORE


def create_and_populate_db():
    df = pd.read_csv("buddymove_holidayiq.csv")

    connection = connect_to_db(db_name="buddymove_holidayiq.sqlite3")

    df.to_sql("review", connection, if_exists='replace')

    return connection


if __name__ == "__main__":
    conn = create_and_populate_db()

    data_count = execute_query(conn, TOTAL_COUNT)
    review_100_more = execute_query(conn, NUM_100_OR_MORE)
    print(data_count)
    print(review_100_more)

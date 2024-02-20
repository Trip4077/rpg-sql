from pandas_helper import create_and_populate_sqlite
from sqlite_example import execute_query
from queries import TOTAL_COUNT, NUM_100_OR_MORE

if __name__ == "__main__":
    conn = create_and_populate_sqlite(
        "buddymove_holidayiq.csv",
        "buddymove_holidayiq.sqlite3",
        "review"
    )

    data_count = execute_query(conn, TOTAL_COUNT)
    review_100_more = execute_query(conn, NUM_100_OR_MORE)
    print(data_count)
    print(review_100_more)

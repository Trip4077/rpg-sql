import pandas as pd
from sqlite_example import connect_to_db


def create_and_populate_sqlite(file, db_name, table_name):
    df = pd.read_csv(file)

    connection = connect_to_db(db_name=db_name)

    df.to_sql(table_name, connection, if_exists='replace')

    return connection

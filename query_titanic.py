from pg_helper import connect_to_pg, fetch_data

DB_NAME = 'fvqbnsjx'
USER_NAME = 'fvqbnsjx'
HOST_NAME = 'jelani.db.elephantsql.com'
PASSWORD = 'EsCx6Ar_O163G7ho46ymEn8t5ALXckle'

SELECT_ALL_TITANIC_DATA = '''
  SELECT * FROM titanic;
'''

SURVIVED_COUNT = '''
    SELECT COUNT(*) FROM titanic AS t
    WHERE "Survived" = 1;
'''

DECEASED_COUNT = '''
    SELECT COUNT(*) FROM titanic AS t
    WHERE "Survived" = 0;
'''

PCLASS_COUNTS = '''
    SELECT "Pclass", COUNT(*) as class_count
    FROM titanic
    GROUP BY "Pclass"
    ORDER BY "Pclass";
'''

SURVIVAL_VALUES_BY_PCLASS = '''
    SELECT "Pclass", "Survived", COUNT(*) as count
    FROM titanic
    GROUP BY "Pclass", "Survived"
    ORDER BY "Pclass", "Survived";
'''

AVERAGE_AGE_BY_SURVIVAL = '''
    SELECT "Survived", AVG("Age") AS average_age
    FROM titanic
    WHERE "Age" > 0
    GROUP BY "Survived"
    ORDER BY "Survived";
'''

AVERAGE_AGE_BY_CLASS = '''
    SELECT "Pclass", AVG("Age") AS average_age
    FROM titanic
    WHERE "Age" > 0
    GROUP BY "Pclass"
    ORDER BY "Pclass";
'''

AVERAGE_FARE_BY_CLASS = '''
    SELECT "Pclass", AVG("Fare") AS average_fare
    FROM titanic
    GROUP BY "Pclass"
    ORDER BY "Pclass";
'''

AVERAGE_FARE_BY_SURVIVAL = '''
    SELECT "Survived", AVG("Fare") AS average_fare
    FROM titanic
    GROUP BY "Survived"
    ORDER BY "Survived";
'''

AVERAGE_RELATIVES_BY_CLASS = '''
    SELECT "Pclass", AVG("SibSp") AS average_relatives
    FROM titanic
    GROUP BY "Pclass"
    ORDER BY "Pclass";
'''

AVERAGE_RELATIVES_BY_SURVIVAL = '''
    SELECT "Survived", AVG("SibSp") AS average_relatives
    FROM titanic
    GROUP BY "Survived"
    ORDER BY "Survived";
'''

if __name__ == '__main__':
    pg_conn, pg_cursor = connect_to_pg(DB_NAME, USER_NAME, PASSWORD, HOST_NAME)

    # How many passengers survived, and how many died?
    survived_result = fetch_data(pg_cursor, SURVIVED_COUNT)
    died_result = fetch_data(pg_cursor, DECEASED_COUNT)

    survived = survived_result[0][0]
    died = died_result[0][0]

    print(survived, died)

    # How many passengers were in each class?
    pclass_result = fetch_data(pg_cursor, PCLASS_COUNTS)

    print(pclass_result)

    # How many passengers survived/died within each class?
    survived_by_pclass_result = fetch_data(
        pg_cursor, SURVIVAL_VALUES_BY_PCLASS
    )

    print(survived_by_pclass_result)

    # What was the average age of survivors vs nonsurvivors?
    average_ages = fetch_data(pg_cursor, AVERAGE_AGE_BY_SURVIVAL)
    average_ages = [
        (average_ages[0][0], float(average_ages[0][1])),
        (average_ages[1][0], float(average_ages[1][1]))
    ]

    print(average_ages)

    # What was the average age of each passenger class?
    average_ages_class = fetch_data(pg_cursor, AVERAGE_AGE_BY_CLASS)
    average_ages_class = [
        (average_ages_class[0][0], float(average_ages_class[0][1])),
        (average_ages_class[1][0], float(average_ages_class[1][1])),
        (average_ages_class[2][0], float(average_ages_class[2][1]))
    ]

    print(average_ages_class)

    # What was the average fare by passenger class? By survival?
    average_fare_by_class = fetch_data(pg_cursor, AVERAGE_FARE_BY_CLASS)
    average_fare_by_survival = fetch_data(pg_cursor, AVERAGE_FARE_BY_SURVIVAL)

    average_fare_by_class = [
        (average_fare_by_class[0][0], float(average_fare_by_class[0][1])),
        (average_fare_by_class[1][0], float(average_fare_by_class[1][1])),
        (average_fare_by_class[2][0], float(average_fare_by_class[2][1]))
    ]

    average_fare_by_survival = [
        (average_fare_by_survival[0][0],
         float(average_fare_by_survival[0][1])),
        (average_fare_by_survival[1][0],
         float(average_fare_by_survival[1][1]))
    ]

    print(average_fare_by_class)
    print(average_fare_by_survival)

    # How many siblings/spouses aboard on average, by passenger class?
    # By survival?

    average_relatives_by_class = fetch_data(
        pg_cursor, AVERAGE_RELATIVES_BY_CLASS)
    average_relatives_by_survival = fetch_data(
        pg_cursor, AVERAGE_RELATIVES_BY_SURVIVAL)

    average_relatives_by_class = [
        (average_relatives_by_class[0][0],
         float(average_relatives_by_class[0][1])),
        (average_relatives_by_class[1][0],
         float(average_relatives_by_class[1][1])),
        (average_relatives_by_class[2][0],
         float(average_relatives_by_class[2][1]))
    ]

    average_relatives_by_survival = [
        (average_relatives_by_survival[0][0],
         float(average_relatives_by_survival[0][1])),
        (average_relatives_by_survival[1][0],
         float(average_relatives_by_survival[1][1]))
    ]

    print(average_relatives_by_class)
    print(average_relatives_by_survival)

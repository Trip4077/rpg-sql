from pymongo import MongoClient
from sqlite_example import execute_query, connect_to_db
from queries import SELECT_ALL_CHARACTERS_AND_INVENTORY, SELECT_ARMORY_WEAPONS

DB_NAME = 'RPG_DB'
PASSWORD = 'passforschool'


def sqlite_to_mongo(list_data=[]):
    formatted_character_dict = {}

    for character in list_data:
        if formatted_character_dict.get(character[0]) is None:
            formatted_character_dict[character[0]] = {
                "name": character[1],
                "level": character[2],
                "exp": character[3],
                "hp": character[4],
                "strength": character[5],
                "intelligence": character[6],
                "dexterity": character[7],
                "wisdom": character[8],
                "items": [],
                "weapons": []
            }

        item_id = character[12]
        formatted_character_dict[character[0]]["items"].append(character[13])

        if item_id in weapon_ids:
            formatted_character_dict[character[0]
                                     ]["weapons"].append(character[13])

    return list(formatted_character_dict.values())


def mongo_connect(collection='characters'):
    client = MongoClient(
        '''mongodb+srv://bernardwebdev:passforschool@rpg.rymcixn.mongodb.net/?retryWrites=true&w=majority&appName=rpg'''
    )

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client


if __name__ == '__main__':
    sqlite_conn = connect_to_db()

    character_result = execute_query(
        sqlite_conn, SELECT_ALL_CHARACTERS_AND_INVENTORY
    )

    weapon_result = execute_query(sqlite_conn, SELECT_ARMORY_WEAPONS)
    weapon_ids = [item[0] for item in weapon_result]

    formatted_characters = sqlite_to_mongo(character_result)

    mongo_client = mongo_connect()
    db = mongo_client.characters

    result = db.characters.insert_many(formatted_characters)

    print(result)

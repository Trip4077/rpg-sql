from mongo import mongo_connect

if __name__ == "__main__":
    mongo_client = mongo_connect()
    characters_collection = mongo_client.characters.characters

    # How many total Characters are there?
    total_count = characters_collection.count_documents({})

    print(total_count)

    # How many total Items?
    pipeline = [
        {"$unwind": "$items"},
        {"$group": {"_id": None, "totalItems": {"$sum": 1}}}
    ]

    result = list(characters_collection.aggregate(pipeline))
    item_count = result[0]['totalItems']

    print(item_count)

    # How many of the Items are Weapons? How many are not?
    pipeline = [
        {"$unwind": "$weapons"},
        {"$group": {"_id": None, "totalWeapons": {"$sum": 1}}}
    ]

    result = list(characters_collection.aggregate(pipeline))
    weapon_count = result[0]['totalWeapons']

    print(weapon_count)
    print(item_count - weapon_count)

    # How many Items does each Character have? (Return first 20 rows)
    pipeline = [
        {
            "$project": {
                "_id": "$_id",
                "name": "$name",
                "itemNameCount": {"$size": "$items"}
            }
        },
        {
            "$limit": 20
        }
    ]

    inventory_counts = list(characters_collection.aggregate(pipeline))

    print(inventory_counts)

    # How many Weapons does each Character have? (Return first 20 rows)
    pipeline = [
        {
            "$project": {
                "_id": "$_id",
                "name": "$name",
                "weaponNameCount": {"$size": "$weapons"}
            }
        },
        {
            "$limit": 20
        }
    ]

    weapon_counts = list(characters_collection.aggregate(pipeline))

    print(weapon_counts)

    # On average, how many Items does each Character have?
    pipeline = [
        {
            "$project": {
                "_id": None,
                "itemNameCount": {"$size": "$items"}
            }
        },
        {
            "$group": {
                "_id": None,
                "totalItemCount": {"$sum": "$itemNameCount"},
                "documentCount": {"$sum": 1}
            }
        },
        {
            "$project": {
                "_id": None,
                "averageItemCount": {
                    "$divide": ["$totalItemCount", "$documentCount"]
                }
            }
        }
    ]

    average_items_result = list(characters_collection.aggregate(pipeline))
    average_items = average_items_result[0]["averageItemCount"]

    print(average_items)

    # On average, how many Weapons does each Character have?
    pipeline = [
        {
            "$project": {
                "_id": None,
                "weaponNameCount": {"$size": "$weapons"}
            }
        },
        {
            "$group": {
                "_id": None,
                "totalWeaponCount": {"$sum": "$weaponNameCount"},
                "documentCount": {"$sum": 1}
            }
        },
        {
            "$project": {
                "_id": None,
                "averageWeaponCount": {
                    "$divide": ["$totalWeaponCount", "$documentCount"]
                }
            }
        }
    ]

    average_weapons_result = list(characters_collection.aggregate(pipeline))
    average_weapons = average_weapons_result[0]["averageWeaponCount"]

    print(average_weapons)

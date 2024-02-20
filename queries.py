SELECT_CHARACTERS = 'SELECT * FROM charactercreator_character'

SELECT_CHARACTERS_ID_AND_NAME = (
    'SELECT character_id, name '
    'FROM charactercreator_character;'
)

SELECT_5_NAME_AND_HP = (
    'SELECT name, hp '
    'FROM charactercreator_character '
    'LIMIT 5;'
)

SELECT_CHARACTER_ID_80 = (
    'SELECT * '
    'FROM charactercreator_character '
    'WHERE character_id = 80;'
)

SELECT_CHARACTER_ID_BETWEEN_80_AND_100 = (
    'SELECT character_id, name '
    'FROM charactercreator_character '
    'WHERE character_id >= 80 AND character_id <= 100;'
)

SELECT_CHARACTER_ID_BETWEEN_5_AND_12 = (
    'SELECT character_id, name '
    'FROM charactercreator_character '
    'WHERE character_id BETWEEN 5 AND 12;'
)

SELECT_DISTINCT_NAMES = (
    'SELECT DISTINCT name '
    'FROM charactercreator_character;'
)

COUNT_CHARACTER_NAMES = (
    'SELECT name, COUNT(*) '
    'FROM charactercreator_character '
    'GROUP BY name '
    'ORDER BY COUNT(*) DESC;'
)

SELECT_NAME_COUNT_2 = (
    'SELECT name, COUNT(*) AS num_characters '
    'FROM charactercreator_character '
    'GROUP BY name '
    'HAVING num_characters = 2 '
    'ORDER BY name DESC;'
)

SELECT_STRENGTH_WITH_PET = (
    'SELECT strength, has_pet '
    'FROM charactercreator_character AS ccc '
    'JOIN charactercreator_mage AS ccm '
    'ON ccc.character_id = ccm.character_ptr_id;'
)

SELECT_AVERAGE_ARMORY_ITEM_WEIGHT = (
    'SELECT ccm.name, AVG(ai.weight) AS avg_item_weight '
    'FROM charactercreator_character AS ccm '
    'JOIN charactercreator_character_inventory AS cci '
    'ON ccm.character_id = cci.character_id '
    'JOIN armory_item AS ai '
    'ON ai.item_id = cci.item_id '
    'GROUP BY ccm.character_id;'
)

TOTAL_CHARACTERS = '''
SELECT COUNT(*) AS character_count
FROM charactercreator_character;
'''

TOTAL_SUBCLASS = '''
SELECT COUNT(*) AS necromancer_count
FROM charactercreator_necromancer;
'''

TOTAL_ITEMS = '''
SELECT COUNT(*) AS item_count
FROM armory_item;
'''

WEAPONS = '''
SELECT COUNT(*) AS weapon_count
FROM armory_item AS ai
JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id;
'''

NON_WEAPONS = '''
SELECT COUNT(*) AS non_weapon_count
FROM armory_item AS ai
LEFT JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
WHERE aw.item_ptr_id IS NULL;
'''

CHARACTER_ITEMS = '''
SELECT ccc.character_id, ccc.name, COUNT(cci.item_id) AS num_items
FROM charactercreator_character AS ccc
JOIN charactercreator_character_inventory AS cci
ON ccc.character_id = cci.character_id
JOIN armory_item AS ai
ON ai.item_id = cci.item_id
GROUP BY ccc.character_id, ccc.name
LIMIT 20;
'''

CHARACTER_WEAPONS = '''
SELECT ccc.character_id, ccc.name, COUNT(aw.item_ptr_id) AS weapon_count
FROM charactercreator_character AS ccc
JOIN charactercreator_character_inventory AS cci
ON ccc.character_id = cci.character_id
JOIN armory_item AS ai
ON ai.item_id = cci.item_id
LEFT JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
GROUP BY ccc.character_id, ccc.name
LIMIT 20;
'''

AVG_CHARACTER_ITEMS = '''
SELECT AVG(num_items) AS avg_item_count
FROM (
  SELECT ccc.character_id, ccc.name, COUNT(cci.item_id) AS num_items
  FROM charactercreator_character AS ccc
  JOIN charactercreator_character_inventory AS cci
  ON ccc.character_id = cci.character_id
  JOIN armory_item AS ai
  ON ai.item_id = cci.item_id
  GROUP BY ccc.character_id, ccc.name
) AS subquery;
'''

AVG_CHARACTER_WEAPONS = '''
SELECT AVG(weapon_count) AS avg_item_count
FROM (
  SELECT ccc.character_id, ccc.name, COUNT(aw.item_ptr_id) AS weapon_count
  FROM charactercreator_character AS ccc
  JOIN charactercreator_character_inventory AS cci
  ON ccc.character_id = cci.character_id
  JOIN armory_item AS ai
  ON ai.item_id = cci.item_id
  LEFT JOIN armory_weapon AS aw
  ON ai.item_id = aw.item_ptr_id
  GROUP BY ccc.character_id, ccc.name
) AS subquery
'''

TOTAL_COUNT = '''
SELECT COUNT(*) AS num_rows
FROM review
'''

NUM_100_OR_MORE = '''
SELECT COUNT(*) as num_100_or_more
FROM review AS r
WHERE r.Nature <= 100 
AND r.Shopping <= 100
'''

CREATE_TEST_TABLE = '''
CREATE TABLE IF NOT EXISTS test_table 
(
  "id" SERIAL NOT NULL PRIMARY KEY,
  "name" VARCHAR(200) NOT NULL,
  "age" INT NOT NULL,
  "country_of_origin" VARCHAR(200) NOT NULL
);
'''

INSERT_TEST_TABLE = '''
INSERT INTO test_table
(
  "name",
  "age",
  "country_of_origin"
)
VALUES (
  'Bernard Johnson',
  30,
  'US'
)
'''

DROP_TEST_TABLE = '''
DROP TABLE IF EXISTS test_table
'''

CREATE_CHARACTER_TABLE = '''
CREATE TABLE IF NOT EXISTS character
(
  "character_id" SERIAL NOT NULL PRIMARY KEY,
  "name" VARCHAR(30),
  "level" INT NOT NULL,
  "exp" INT NOT NULL,
  "hp" INT NOT NULL,
  "strength" INT NOT NULL,
  "intelligence" INT NOT NULL,
  "dexterity" INT NOT NULL,
  "wisdom" INT NOT NULL
);
'''

INSERT_BERNARD = '''
INSERT INTO character
(
  "name",
  "level",
  "exp",
  "hp",
  "strength",
  "intelligence",
  "dexterity",
  "wisdom"
)
VALUES 
(
  'Bernard',
  10,
  1000,
  200,
  10,
  15,
  12,
  13
)
'''

DROP_CHARACTER_TABLE = '''
DROP TABLE IF EXISTS character
'''


def select_name_by_id(id):
    return (
        'SELECT character_id, name '
        'FROM charactercreator_character '
        f"WHERE character_id = {id};"
    )


def insert_new_character(
    name, level, exp, hp,
    strength, intelligence, dexterity, wisdom
):
    return f'''
        INSERT INTO character
        (
            "name",
            "level",
            "exp",
            "hp",
            "strength",
            "intelligence",
            "dexterity",
            "wisdom"
        )
        VALUES
        (
            '{name}',
            {level},
            {exp},
            {hp},
            {strength},
            {intelligence},
            {dexterity},
            {wisdom}
        )
    '''

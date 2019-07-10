from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://admin:admin@c4e34-cluster-ywuyq.mongodb.net/test?retryWrites=true&w=majority")

# create / get database
first_database = client.demo_database

# create / get collection
first_collection = first_database["demo_collection"]

first_document = {
  "name": "FO4",
  "description": "Football game",
}

list_document = [
  {
    "name": "LoL",
    "description": "MOBA game"
  },
  {
    "name": "Dota",
    "description": "Valve",
  },
  {
    "name": "Auto chess",
    "description": "A part of DOTA"
  }
]

# 1. CREATE
# 1.1 Create One
# first_collection.insert_one(first_document)

# 1.2 Create Many
# first_collection.insert_many(list_document)

# 2. READ
# 2.1 READ ALL
# lazy loading
# games = first_collection.find()

# for game in games:
#   print(game)

# fo4_games = first_collection.find({"name": "FO4"})

# for fo4 in fo4_games:
#   print(fo4)

# 2.1 READ ONE
# dota_game = first_collection.find_one({"_id": ObjectId("5d2056f368a3ff27d0199245")})
# print(dota_game)

# 3. UPDATE
# query
# dota_game = first_collection.find_one({"_id": ObjectId("5d2056f368a3ff27d0199245")})
# new_value = { "$set": { "name": "DOTA" } }

# first_collection.update_one(dota_game, new_value)

# 4. DELETE
dota_game = first_collection.find_one({"_id": ObjectId("5d2056f368a3ff27d0199245")})
if dota_game is not None:
  first_collection.delete_one(dota_game)
else:
  print("Not found")
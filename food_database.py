from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@c4e34-cluster-ywuyq.mongodb.net/test?retryWrites=true&w=majority")

food_database = client.food_db

Foods = food_database["Foods"]

Users = food_database["Users"]

users_list = [
    {
        "username": "hduc",
        "password": "12345"
    },
    {
        "username": "mdat",
        "password": "123"
    },
    {
        "username": "haanh",
        "password": "1234"
    }
]

Users.insert_many(users_list)

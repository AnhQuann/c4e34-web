from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@c4e34-cluster-ywuyq.mongodb.net/test?retryWrites=true&w=majority")

food_database = client.food_db

Foods = food_database["Foods"]

all_foods = [
    {
        "title": "Bún đậu",
        "description": "Rất ngon",
        "type": "food",
        "link": "https://justfly.vn/Upload/2018/04/bun-dau-mam-tom-25_04_2018_12_53.png"
    },
    {
        "title": "Thịt rán",
        "description": "Bình thường",
        "type": "food",
        "link": "https://giadinh.tv/wp-content/uploads/2018/10/Cach-lam-mon-thit-ran-ngon_1.jpg"
    },
    {
        "title": "Phở",
        "description": "Tuyệt",
        "type": "drink",
        "link": "https://cdn.tgdd.vn/Files/2018/06/14/1095399/huong-dan-chi-tiet-cach-nau-pho-bo-thom-ngon-bo-duong-cho-ca-nha.png"
    }
]

# Foods.insert_many(all_foods)
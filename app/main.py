import pymongo
from pprint import pprint

connection_string = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"
client = pymongo.MongoClient(connection_string)
db = client["IranMalDB"]
collection = db["tweets"]

for doc in collection.find().limit(5):
    pprint(doc)

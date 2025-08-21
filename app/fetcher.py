import pymongo
import os
class MongoLoader:
    def __init__(self):


        self.MONGO_USER = os.getenv("MONGO_USER", "IRGC")
        self.MONGO_PASS = os.getenv("MONGO_PASS", "iraniraniran")
        self.MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")
        self.connection_string=os.getenv("connection_string","mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")

        self.myclient = pymongo.MongoClient(self.connection_string)
        self.mydb = self.myclient[self.MONGO_DB]

    def get_all_data(self):

        mycol = self.mydb["enemy_soldiers"]
        return list(mycol.find())
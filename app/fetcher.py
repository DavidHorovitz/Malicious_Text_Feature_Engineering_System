import pymongo
import os
import pandas as pd
class MongoLoader:
    def __init__(self):


        self.MONGO_USER = os.getenv("MONGO_USER", "IRGC")
        self.MONGO_PASS = os.getenv("MONGO_PASS", "iraniraniran")
        self.MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")

        self.connection_string=os.getenv("connection_string",f"mongodb+srv://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_DB}.gurutam.mongodb.net/")

        self.myclient = pymongo.MongoClient(self.connection_string)
        self.mydb = self.myclient[self.MONGO_DB]

    def get_all_data(self):

        mycol = self.mydb["tweets"]
        df=pd.DataFrame(list(mycol.find()))
        return df








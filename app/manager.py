from tkinter.font import names

from processor import Processing as pr
from fetcher import MongoLoader as ml

class Manager:
    def manager(self):
        loader = ml()
        df = loader.get_all_data()

        processor = pr()
        processor.df = df
        processor.rare_word_in_text()
        processor.find_text_emotion()
        return processor.df


if __name__ == "__main__":
    a = Manager()
    df_result = a.manager()
    # print(df_result.head())
    # print(df_result.columns)






# connection_string = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"
# client = pymongo.MongoClient(connection_string)
# db = client["IranMalDB"]
# collection = db["tweets"]
#
# for doc in collection.find().limit(5):
#     pprint(doc)
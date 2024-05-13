import pymongo


class ConnectMongo:

    def __init__(self):
        self.uri = "mongodb+srv://2deram:2deram@tutoria.wxrtz25.mongodb.net/"
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client["adoptame"]
    def get_collection_db(self, collection_name):
        collections = self.db.list_collection_names()
        if collection_name in collections:
            return self.db.get_collection(collection_name)
        else:
            return self.db.create_collection(collection_name)
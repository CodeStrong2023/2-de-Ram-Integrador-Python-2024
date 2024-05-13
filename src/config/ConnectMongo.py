import pymongo


class ConnectMongo:

    def __init__(self):
        self.db = self.connect()

    def connect(self):
        uri = "mongodb+srv://2deram:2deram@tutoria.wxrtz25.mongodb.net/"
        client = pymongo.MongoClient(uri)
        db = client["adoptame"]
        return db

    def get_collection_db(self, collection_name):
        collections = self.db.list_collection_names()
        if collection_name in collections:
            return self.db.get_collection(collection_name)
        else:
            return self.db.create_collection(collection_name)

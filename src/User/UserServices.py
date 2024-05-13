from src.config.MongoConfig import MongoConfig


class UserServices:
    collections = None


    def __init__(self, db):
        self.mongo = MongoConfig().db
        self.create_collection()
        self.user_collection = self.mongo.get_collection("user")
    def create_collection(self):
        collections = self.mongo.list_collection_names()
        for name in collections:
            if name == "user":
                return False
            else:
                self.mongo.create_collection("user")

    def create_user(self, user):
        self.user_collection.insert_one(user)

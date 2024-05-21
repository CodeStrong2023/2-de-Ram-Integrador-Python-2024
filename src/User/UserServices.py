from bson import ObjectId

from User.UserModel import *
from config.ConnectMongo import ConnectMongo
from utils.StrUtils import StrUtils


class UserServices:
    def __init__(self):
        self.connection = ConnectMongo()
        self.user_collection = self.connection.db.get_collection("users")

    def create_user(self):
        StrUtils.create_header("Registro de Usuario")
        user = UserModel().create_user()
        self.user_collection.insert_one(user)
        print("Usuario Registrado")

    def get_all_users(self):
        return self.user_collection.find()

    def get_user_by_id(self, user_id):
        return self.user_collection.find_one({"_id": ObjectId(user_id)})

    def get_user_by_email(self, email):
        return self.user_collection.find_one({"email": email})

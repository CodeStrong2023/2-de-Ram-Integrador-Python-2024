
from src.User.UserModel import *
from src.config.ConnectMongo import ConnectMongo
from src.utils.InputUtils import InputUtils
from src.utils.StrUtils import StrUtils
class UserServices:
    def __init__(self):
        self.connection = ConnectMongo()
        self.user_collection = self.connection.db.get_collection("users")
    def create_user(self):
        StrUtils.create_header("Registro de Usuario")
        user = UserModel().create_user()
        self.user_collection.insert_one(user)
        print("Usuario Registrado")


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
        user_model = UserModel()
        name = InputUtils.str_input("Ingrese su nombre completo: ")
        email = InputUtils.str_input("Ingrese su email: ")
        password = InputUtils.str_input("Ingrese su password: ")
        age = InputUtils.int_input("Ingrese su edad: ")
        dni = InputUtils.str_input("Ingrese su dni: ")
        user = user_model.create_user(name, email, password, age, dni)
        self.user_collection.insert_one(user)
        print("Usuario Registrado")


from src.User.UserModel import *
from src.config.ConnectMongo import ConnectMongo
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

    def delete_user(self, user_id, current_user):
        user = self.user_collection.find_one({"_id": user_id})
        if user:
            if self.user_validator.validate_admin_role(current_user):
                self.user_collection.delete_one({"_id": user_id})
                print("Usuario eliminado con éxito")
            else:
                print("No tienes permisos para eliminar usuarios")
        else:
            print("No se encontró ningún usuario con el ID proporcionado")

from bson import ObjectId

from src.Pet.PetManagementMenu import PetService
from src.User.UserModel import *
from src.config.ConnectMongo import ConnectMongo
from src.utils.StrUtils import StrUtils


class UserServices:
    def __init__(self):
        self.connection = ConnectMongo()
        self.user_collection = self.connection.db.get_collection("users")

    def create_user(self):
        from auth.MainMenu import MainMenu
        StrUtils.create_header("Registro de Usuario")
        user = UserModel().create_user()
        self.user_collection.insert_one(user)
        print("Usuario Registrado")
        MainMenu().display_menu()

    # Obtiene todos los usuarios
    def get_all_users(self):
        return self.user_collection.find()

    # Obtiene un usuario por su id
    def get_user_by_id(self, user_id):
        return self.user_collection.find_one({"_id": ObjectId(user_id)})

    # Obtiene un usuario por su email
    def get_user_by_email(self, email):
        return self.user_collection.find_one({"email": email})

    # Eliminamos un usuario cambiando su status a False
    def delete_user(self, user_id):
        self.user_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": {"status": False}}
        )
        print("Usuario Eliminado")

    # Actualizamos un usuario con la información recibida
    def update_user(self, user_id, data):
        self.user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
        print("Usuario Actualizado")

    # Agregamos una mascota a un usuario
    def add_pet_to_user(self, user_id, pet_id):
        pet = PetService().get_pet_by_id(pet_id)
        self.user_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$push": {"pets": pet}}
        )
        return self.user_collection.find_one({"_id": ObjectId(user_id)})

from src.config.ConnectMongo import ConnectMongo
from src.Pet.PetModel import *
from src.utils.StrUtils import StrUtils

class PetService:
    def __init__(self):
        self.connection = ConnectMongo()
        self.user_collection = self.connection.db.get_collection("pets")
    def create_user(self):
        StrUtils.create_header("Registro de Mascotas")
        pet = PetModel().create_pet()
        self.user_collection.insert_one(pet)
        print("Mascota registrada con éxito")
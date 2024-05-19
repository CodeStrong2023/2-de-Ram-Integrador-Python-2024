from src.config.ConnectMongo import ConnectMongo
from src.Pet.PetModel import *
from src.utils.StrUtils import StrUtils

class PetService:
    def __init__(self):
        self.connection = ConnectMongo()
        self.pet_collection = self.connection.db.get_collection("pets")
    def create_pet(self):
        StrUtils.create_header("Registro de Mascotas")
        pet = PetModel().create_pet()
        self.user_collection.insert_one(pet)
        print("Mascota registrada con éxito")

    #Obtener todaslas mascotas
    '''Devuelve un arreglo de mascotas con todas las mascotas en la BBDD'''
    def get_all_pets(self):
        pets = self.pet_collection.find()
        return [pet for pet in pets]

    #Obtener mascota por su ID
    def get_pet_by_id(self, pet_id):
        pet = self.pet_collection.find_one({"_id": pet_id})
        return pet

    #Guardar Mascota
    def save_pet(self, pet_data):
        self.pet_collection.insert_one(pet_data)
        print("Mascota guardada con éxito")

    #Actualizar Mascota
    '''Recibe el ID de una mascota y los nuevos datos de la mascota a editar. 
    Este método actualiza los datos de la mascota en la colección "pets" 
    de la base de datos MongoDB utilizando el método update_one()'''
    def update_pet(self, pet_id, pet_data):
        self.pet_collection.update_one({"_id": pet_id}, {"$set": pet_data})
        print("Mascota actualizada con éxito")

    #Borrar una mascota por su id
    def delete_pet(self, pet_id):
        result = self.pet_collection.delete_one({"_id": pet_id})
        if result.deleted_count > 0:
            print("Mascota eliminada con éxito")
        else:
            print("No se encontró ninguna mascota con el ID proporcionado")
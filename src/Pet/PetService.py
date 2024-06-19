from src.config.ConnectMongo import ConnectMongo
from src.pet.PetModel import *
from src.utils.StrUtils import StrUtils


# Clase que gestiona las operaciones de la mascota en la base de datos de MongoDB
class PetService:
    
    # Constructor de la clase
    def __init__(self):
        self.connection = ConnectMongo()
        self.pet_collection = self.connection.get_collection_db("pets")

    # Método para guardar una nueva mascota en la base de datos
    def save_pet(self, pet_data):
        # Utilizar el método insert_one de la colección para insertar la mascota
        inserted_pet = self.pet_collection.insert_one(pet_data)
        return inserted_pet.inserted_id  # Devolver el ID de la mascota insertada

    # Crear Mascota
    def create_pet(self):
        StrUtils.create_header("Registro de Mascotas")
        pet = PetModel().create_pet()
        self.pet_collection.insert_one(pet)
        print("Mascota registrada con éxito")

    # Obtener todas las mascotas
    '''Devuelve un arreglo de mascotas con todas las mascotas en la BBDD'''
    def get_all_pets(self):
        pets = self.pet_collection.find()
        return [pet for pet in pets]

    # Obtener mascota por su ID
    def get_pet_by_id(self, pet_id):
        try:
            pet_id = ObjectId(pet_id)
            pet = self.pet_collection.find_one({"_id": pet_id})
            return pet
        except Exception as e:
            print("Error al buscar la mascota por ID:", e)
            return None



    # Actualizar Mascota
    '''Recibe el ID de una mascota y los nuevos datos de la mascota a editar. 
    Este método actualiza los datos de la mascota en la colección "pets" 
    de la base de datos MongoDB utilizando el método update_one()'''
    def update_pet(self, pet_id, pet_data):
        self.pet_collection.update_one({"_id": pet_id}, {"$set": pet_data})
        print("Mascota actualizada con éxito")

    def delete_pet(self, pet_id):
        result = self.pet_collection.delete_one({"_id": ObjectId(pet_id)})
        if result.deleted_count == 1:
            print("Mascota eliminada con éxito")
        else:
            print("No se encontró la mascota con ese ID")

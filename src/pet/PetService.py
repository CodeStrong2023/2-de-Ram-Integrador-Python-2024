from pymongo.errors import PyMongoError

from src.config.ConnectMongo import ConnectMongo
from src.pet.PetModel import *
from src.utils.StrUtils import StrUtils
from bson import ObjectId


# Clase que gestiona las operaciones de la mascota en la base de datos de MongoDB
class PetService:

    # Constructor de la clase
    def __init__(self):
        self.connection = ConnectMongo()
        self.pet_collection = self.connection.get_collection_db("pets")

    # Método para guardar una nueva mascota en la base de datos
    def save_pet(self, pet_data):
        try:
            # Intenta insertar el documento en la colección
            inserted_pet = self.pet_collection.insert_one(pet_data)
            return inserted_pet.inserted_id  # Devolver el ID de la mascota insertada
        except PyMongoError as e:
            # Maneja errores específicos de PyMongo
            print(f"Ocurrió un error con la base de datos: {e}")
            return None
        except Exception as e:
            # Maneja cualquier otro tipo de error
            print(f"Ocurrió un error inesperado: {e}")
            return None

    # Crear Mascota
    def create_pet(self):
        try:
            StrUtils.create_header("Registro de Mascotas")

            # Intenta crear el objeto pet
            try:
                pet = PetModel().create_pet()
            except Exception as e:
                print(f"Ocurrió un error al crear la mascota: {e}")
                return

            # Intenta insertar el objeto pet en la base de datos
            try:
                self.pet_collection.insert_one(pet)
                print("Mascota registrada con éxito")
            except PyMongoError as e:
                print(f"Ocurrió un error con la base de datos: {e}")
        except Exception as e:
            # Maneja cualquier otro tipo de error
            print(f"Ocurrió un error inesperado: {e}")

    # Obtener todas las mascotas
    '''Devuelve un arreglo de mascotas con todas las mascotas en la BBDD'''

    def get_all_pets(self):
        try:
            pets = self.pet_collection.find()
            return [pet for pet in pets]
        except PyMongoError as e:
            # Maneja errores específicos de PyMongo
            print(f"Ocurrió un error con la base de datos: {e}")
            return []
        except Exception as e:
            # Maneja cualquier otro tipo de error
            print(f"Ocurrió un error inesperado: {e}")
            return []

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

        try:
            # Verifica que pet_id sea un ObjectId válido
            if not ObjectId.is_valid(pet_id):
                print("El ID proporcionado no es válido.")
                return

            # Intenta convertir pet_id a ObjectId
            pet_oid = ObjectId(pet_id)

            # Intenta actualizar el documento en la colección
            result = self.pet_collection.update_one({"_id": pet_oid}, {"$set": pet_data})

            # Verifica si se actualizó algún documento
            if result.matched_count == 0:
                print("No se encontró la mascota con ese ID")
            else:
                print("Mascota actualizada con éxito")

        except PyMongoError as e:
            # Maneja errores específicos de PyMongo
            print(f"Ocurrió un error con la base de datos: {e}")
        except Exception as e:
            # Maneja cualquier otro tipo de error
            print(f"Ocurrió un error inesperado: {e}")


        pet = self.pet_collection.update_one({"_id": ObjectId(pet_id)}, {"$set": pet_data})

        print("Mascota actualizada con éxito")


    def delete_pet(self, pet_id):
        try:
            # Verifica que pet_id sea un ObjectId válido
            if not ObjectId.is_valid(pet_id):
                print("El ID proporcionado no es válido.")
                return

            # Intenta convertir pet_id a ObjectId
            pet_oid = ObjectId(pet_id)

            # Intenta eliminar el documento de la colección
            result = self.pet_collection.delete_one({"_id": pet_oid})

            # Verifica si se eliminó algún documento
            if result.deleted_count == 1:
                print("Mascota eliminada con éxito")
            else:
                print("No se encontró la mascota con ese ID")

        except PyMongoError as e:
            # Maneja errores específicos de PyMongo
            print(f"Ocurrió un error con la base de datos: {e}")
        except Exception as e:
            # Maneja cualquier otro tipo de error
            print(f"Ocurrió un error inesperado: {e}")

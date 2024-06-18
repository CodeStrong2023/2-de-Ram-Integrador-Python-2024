import pymongo
from bson import ObjectId
from src.config.ConnectMongo import ConnectMongo
from src.pet.PetModel import PetModel
from src.utils.StrUtils import StrUtils
from src.utils.InputUtils import InputUtils


# clase que gestiona las operaciones de la mascota en la base de datos de MongoDB
class PetService:
    
    # constructor de la clase 
    def __init__(self):
        self.connection = ConnectMongo()
        self.pet_collection = self.connection.get_collection_db("pets")

    # método que guarda la información de la mascota en la base de datos
    def save_pet(self, pet_data):
        inserted_pet = self.pet_collection.insert_one(pet_data)
        return inserted_pet.inserted_id

    # método que obtiene la información de todas las mascotas en la base de datos
    def create_pet(self):
        StrUtils.create_header("Registro de Mascotas")
        pet = PetModel().create_pet()
        self.pet_collection.insert_one(pet)
        print("Mascota registrada con éxito")

    # método que obtiene la información de todas las mascotas en la base de datos
    def get_all_pets(self):
        pets = self.pet_collection.find()
        return [pet for pet in pets]

    # método que obtiene la información de una mascota por ID
    def get_pet_by_id(self, pet_id):
        try:
            object_id = ObjectId(pet_id)
        except Exception as e:
            print(f"Error al convertir el ID: {e}")
            return None
        pet = self.pet_collection.find_one({"_id": object_id})
        return pet

    # método que actualiza la información de una mascota en la base de datos
    def update_pet(self, pet_id, pet_data):
        try:
            object_id = ObjectId(pet_id)
        except Exception as e:
            print(f"Error al convertir el ID: {e}")
            return
        self.pet_collection.update_one({"_id": object_id}, {"$set": pet_data})
        print("Mascota actualizada con éxito")

    # método que elimina una mascota de la base de datos
    def delete_pet(self, pet_id):
        try:
            object_id = ObjectId(pet_id)
        except Exception as e:
            print(f"Error al convertir el ID: {e}")
            return
        result = self.pet_collection.delete_one({"_id": object_id})
        if result.deleted_count == 1:
            print("Mascota eliminada con éxito")
        else:
            print("No se encontró la mascota")


# clase que gestiona el menú de opciones para la gestión de mascotas en la base de datos de MongoDB
class PetManagementMenu:
    # constructor de la clase
    def __init__(self):
        self.auth_menu = [
            "1 - Registrar Mascota",
            "2 - Mostrar todas las Mascotas",
            "3 - Buscar Mascota por ID",
            "4 - Actualizar Mascota",
            "5 - Eliminar Mascota",
            "6 - Salir"
        ]
        # se crea una instancia de la clase PetService
        self.pet_service = PetService()
        self.fields_map = {
            "_id": "ID",
            "name": "Nombre",
            "species": "Especie",
            "breed": "Raza",
            "age": "Edad",
            "gender": "Género",
            "color": "Color"
        }
    # método que muestra el menú de opciones para la gestión de mascotas 
    def display_menu(self):
        while True:
            for item in self.auth_menu:
                print(item)
            option = InputUtils.int_input("Ingrese una opción: ", 1)
            if option == 1:
                self.register_pet()
            elif option == 2:
                self.show_all_pets()
            elif option == 3:
                self.search_pet_by_id()
            elif option == 4:
                self.update_pet()
            elif option == 5:
                self.delete_pet()
            elif option == 6:
                print("Gracias por su visita")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                
    # método que registra una mascota
    def register_pet(self):
        self.pet_service.create_pet()
        
    # método que muestra todas las mascotas
    def show_all_pets(self):
        pets = self.pet_service.get_all_pets()
        for pet in pets:
            self.display_pet(pet)
            
    # método que busca una mascota por ID
    def search_pet_by_id(self):
        pet_id = InputUtils.str_input("Ingrese el ID de la mascota: ")
        pet = self.pet_service.get_pet_by_id(pet_id)
        if pet:
            self.display_pet(pet)
        else:
            print("Mascota no encontrada.")

    # método que actualiza una mascota 
    def update_pet(self):
        pet_id = InputUtils.str_input("Ingrese el ID de la mascota a actualizar: ")
        pet = self.pet_service.get_pet_by_id(pet_id)
        if pet:
            updated_data = {}
            print("Deje en blanco los campos que no desea actualizar.")
            for key, spanish_key in self.fields_map.items():
                if key != "_id":
                    new_value = InputUtils.str_input(f"Ingrese el nuevo {spanish_key}: ", optional=True)
                    if new_value:
                        updated_data[key] = new_value

            if updated_data:
                self.pet_service.update_pet(pet_id, updated_data)
            else:
                print("No se realizaron cambios.")
        else:
            print("Mascota no encontrada.")

    # método que elimina una mascota
    def delete_pet(self):
        pet_id = InputUtils.str_input("Ingrese el ID de la mascota a eliminar: ")
        self.pet_service.delete_pet(pet_id)

    # método que muestra la información de una mascota
    def display_pet(self, pet):
        print("Información de la Mascota:")
        for key, spanish_key in self.fields_map.items():
            value = pet.get(key, "No disponible")
            print(f"{spanish_key}: {value}")
        print("-" * 20)


# Ejemplo de uso de la clase PetManagementMenu 
if __name__ == "__main__":
    menu = PetManagementMenu()
    menu.display_menu()

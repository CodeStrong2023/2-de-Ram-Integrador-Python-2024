import pymongo
from bson import ObjectId
from src.config.ConnectMongo import ConnectMongo
from src.Pet.PetModel import PetModel
from src.utils.StrUtils import StrUtils
from src.utils.InputUtils import InputUtils

class PetService:
    def __init__(self):
        self.connection = ConnectMongo()
        self.pet_collection = self.connection.get_collection_db("pets")

    def save_pet(self, pet_data):
        inserted_pet = self.pet_collection.insert_one(pet_data)
        return inserted_pet.inserted_id

    def create_pet(self):
        StrUtils.create_header("Registro de Mascotas")
        pet = PetModel().create_pet()
        self.pet_collection.insert_one(pet)
        print("Mascota registrada con éxito")

    def get_all_pets(self):
        pets = self.pet_collection.find()
        return [pet for pet in pets]

    def get_pet_by_id(self, pet_id):
        try:
            object_id = ObjectId(pet_id)
        except Exception as e:
            print(f"Error al convertir el ID: {e}")
            return None
        pet = self.pet_collection.find_one({"_id": object_id})
        return pet

    def update_pet(self, pet_id, pet_data):
        try:
            object_id = ObjectId(pet_id)
        except Exception as e:
            print(f"Error al convertir el ID: {e}")
            return
        self.pet_collection.update_one({"_id": object_id}, {"$set": pet_data})
        print("Mascota actualizada con éxito")

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

class PetManagementMenu:
    def __init__(self):
        self.auth_menu = [
            "1 - Registrar Mascota",
            "2 - Mostrar todas las Mascotas",
            "3 - Buscar Mascota por ID",
            "4 - Actualizar Mascota",
            "5 - Eliminar Mascota",
            "6 - Salir"
        ]
        self.pet_service = PetService()
        self.fields_map = {
            "_id": "ID",
            "name": "Nombre",
            "species": "Especie",
            "breed": "Raza",
            "age": "Edad",
            "gender": "Género",
            "color": "Color",
            "hair": "Tipo de pelo",
            "size": "Tamaño",
            "coat": "Largo del pelaje",
            "energy": "Tipo de energía",
            "sociability": "Sociabilidad"
        }

    def display_menu(self):
        while True:
            for item in self.auth_menu:
                print(item)
            option = InputUtils.int_input("Ingrese una opción: ")
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

    def register_pet(self):
        self.pet_service.create_pet()

    def show_all_pets(self):
        pets = self.pet_service.get_all_pets()
        for pet in pets:
            self.display_pet(pet)

    def search_pet_by_id(self):
        pet_id = InputUtils.str_input("Ingrese el ID de la mascota: ")
        pet = self.pet_service.get_pet_by_id(pet_id)
        if pet:
            self.display_pet(pet)
        else:
            print("Mascota no encontrada.")

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

    def delete_pet(self):
        pet_id = InputUtils.str_input("Ingrese el ID de la mascota a eliminar: ")
        self.pet_service.delete_pet(pet_id)

    def display_pet(self, pet):
        print("Información de la Mascota:")
        for key, spanish_key in self.fields_map.items():
            value = pet.get(key, "No disponible")
            print(f"{spanish_key}: {value}")
        print("-" * 20)

# Ejemplo de uso
if __name__ == "__main__":
    menu = PetManagementMenu()
    menu.display_menu()
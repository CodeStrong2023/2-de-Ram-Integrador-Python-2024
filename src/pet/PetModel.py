from src.utils.InputUtils import InputUtils
from bson import ObjectId


# Clase que modela los datos de la mascota
class PetModel:


    # Constructor de la clase
    def __init__(self):
        self._id_pet = ObjectId()
        self.name = InputUtils.str_input("Ingrese el nombre de la mascota: ")  # nombre
        self.species = InputUtils.str_input("Ingrese la especie de la mascota: ")  # especie
        self.breed = InputUtils.str_input("Ingrese la raza de la mascota: ")  # raza
        self.age = InputUtils.int_input("Ingrese la edad de la mascota: ", 2)  # edad
        self.gender = InputUtils.str_input("Ingrese el género de la mascota: ")  # género
        self.color = InputUtils.str_input("Ingrese el color de la mascota: ")



    # Crear un diccionario con los datos de la mascota
    def create_pet(self):
        pet_data = {
            "id": self._id_pet,
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
            "color": self.color,
        }
        return pet_data

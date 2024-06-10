from src.utils.InputUtils import InputUtils


# Clase que modela los datos de la mascota
class PetModel:
    howMany = 0  # Contador para el número de mascotas

    # Constructor de la clase
    def __init__(self):
        self.name = InputUtils.str_input("Ingrese el nombre de la mascota: ")  # nombre
        self.species = InputUtils.str_input("Ingrese la especie de la mascota: ")  # especie
        self.breed = InputUtils.str_input("Ingrese la raza de la mascota: ")  # raza
        self.age = InputUtils.int_input("Ingrese la edad de la mascota: ", 2)  # edad
        self.gender = InputUtils.str_input("Ingrese el género de la mascota: ")  # género
        self.color = InputUtils.str_input("Ingrese el color de la mascota: ")
        PetModel.howMany += 1
        self._id_pet = PetModel.howMany

    # Crear un diccionario con los datos de la mascota
    def create_pet(self):
        pet_data = {
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
            "color": self.color,
        }
        return pet_data

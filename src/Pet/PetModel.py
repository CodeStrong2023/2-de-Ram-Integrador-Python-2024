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
        self.hair = InputUtils.str_input("Ingrese el tipo de pelo de la mascota: ")  # tipo de pelo: con manchas, atigrado, etc
        self.size = InputUtils.str_input("Ingrese el tamaño de la mascota: ")  # tamaño: grande, pequeño, etc
        self.coat = InputUtils.str_input("Ingrese el largo del pelaje de la mascota: ")  # largo del pelaje: corto, largo, etc
        self.energy = InputUtils.str_input("Ingrese el tipo de energía de la mascota: ")  # tipo de energía: juguetón, ansioso, etc
        self.sociability = InputUtils.str_input("Ingrese la sociabilidad de la mascota: ")  # sociabilidad: introvertido, extrovertido, etc
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
            "hair": self.hair,
            "size": self.size,
            "coat": self.coat,
            "energy": self.energy,
            "sociability": self.sociability
        }
        return pet_data

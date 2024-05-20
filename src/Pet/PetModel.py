from src.utils.InputUtils import InputUtils


class PetModel:

    howMany = 0  # Contador para el número de mascotas

    def __init__(self):
        self.name = InputUtils.str_input("Ingrese el nombre de la mascota: ").character_detector  # nombre
        self.species = InputUtils.str_input("Ingrese la especie de la mascota: ").character_detector  # especie
        self.breed = InputUtils.str_input("Ingrese la raza de la mascota: ").character_detector  # raza
        self.age = InputUtils.int_input("Ingrese la edad de la mascota: ").character_detector  # edad
        self.gender = InputUtils.str_input("Ingrese el género de la mascota: ").character_detector  # género
        self.color = InputUtils.str_input("Ingrese el color de la mascota: ").character_detector
        self.hair = InputUtils.str_input("Ingrese el tipo de pelo de la mascota: ").character_detector  # tipo de pelo: con manchas, atigrado, etc
        self.size = InputUtils.str_input("Ingrese el tamaño de la mascota: ").character_detector  # tamaño: grande, pequeño, etc
        self.coat = InputUtils.str_input("Ingrese el largo del pelaje de la mascota: ").character_detector  # largo del pelaje: corto, largo, etc
        self.energy = InputUtils.str_input("Ingrese el tipo de energía de la mascota: ").character_detector  # tipo de energía: juguetón, ansioso, etc
        self.sociability = InputUtils.str_input("Ingrese la sociabilidad de la mascota: ").character_detector  # sociabilidad: introvertido, extrovertido, etc
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

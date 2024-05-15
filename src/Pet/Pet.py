class Pet:

    howMany = 0

    def __init__(self, name, species, breed, age, color, hair, size, coat, energy, sociability):
        self.name = name  # nombre
        self.species = species  # especie
        self.breed = breed  # raza
        self.age = age  # edad
        self.color = color
        self.hair = hair  # tipo de pelo: con manchas, atigrado, etc
        self.size = size  # tamaño: grande, pequeño, etc
        self.coat = coat  # largo del pelaje: corto, largo, etc
        self.energy = energy  # tipo de energia: jugueton, ansioso, etc
        self.sociability = sociability  # sociabilidad: introvertido, extrovertido, etc
        Pet.howMany += 1
        _id_pet = Pet.howMany

    def __str__(self):
        return f'''
        Mascota:
        Nombre: {self.name}
        Especie: {self.species}
        Raza: {self.breed}
        Edad: {self.age}
        Color: {self.color}
        Tamaño: {self.size}
        Dibujo del pelo: {self.hair}
        Largo del pelo: {self.coat}
        Energía: {self.energy}
        Sociabilidad: {self.sociability}
    '''

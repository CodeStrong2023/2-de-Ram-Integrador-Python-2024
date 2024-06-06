# clase que gestiona la presentación de la información de la mascota 
class PetMenuDisplay:

    # método que muestra el menú de la mascota 
    def display_pet_header(self):
        id_header = "ID".center(28, " ")
        name_header = "NOMBRE".center(30, " ")
        age_header = "EDAD".center(6, " ")
        specie_header = "ESPECIE".center(20, " ")
        gender_header = "GENERO".center(8, " ")
        header = f"|{id_header}|{name_header}|{age_header}|{specie_header}|{gender_header}|"
        print("°" * len(header))
        print(header)
        print("°" * len(header))

    # método que muestra la información de la mascota
    def display_pet(self, pet):
        print(
            f"| {str(pet['_id']).ljust(26)} "
            f"| {str(pet['name']).ljust(28)} "
            f"| {str(pet['age']).ljust(4)} "
            f"| {str(pet['species']).ljust(18)} "
            f"| {str(pet['gender']).ljust(6)} |")
        print("")



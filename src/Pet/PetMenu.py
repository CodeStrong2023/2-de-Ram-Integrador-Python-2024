from src.utils.InputUtils import InputUtils
from src.Pet.PetService import PetService

class PetMenu:
    option = 0

    def __init__(self):
        self.pet_menu = [
            "1 - Mostrar todas las mascotas disponibles",
            "2 - Mostrar una mascota por ID",
            "3 - Eliminar una mascota",
            "4 - Actualizar una mascota",
            "5 - Salir"
        ]

    def display_menu(self):
        for item in self.pet_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        if self.option == 1:
            # Lógica para mostrar todas las mascotas
            pet_service = PetService()
            pet_service.get_all_pets()
        elif self.option == 2:
            pet_id = InputUtils.int_input("Ingrese el ID de la mascota: ")
            # Lógica para mostrar una mascota por ID
            pet_service = PetService()
            pet_service.get_pet_by_id(pet_id)
        elif self.option == 3:
            pet_id = InputUtils.int_input("Ingrese el ID de la mascota a eliminar: ")
            # Lógica para eliminar una mascota
            pet_service = PetService()
            pet_service.delete_pet(pet_id)
        elif self.option == 4:
            pet_id = InputUtils.int_input("Ingrese el ID de la mascota a actualizar: ")
            # Lógica para actualizar una mascota
            pet_service = PetService()
            pet_service.update_pet(pet_id)
        elif self.option == 5:
            print("Gracias por su visita")
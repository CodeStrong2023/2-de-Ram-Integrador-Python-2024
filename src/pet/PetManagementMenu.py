from src.pet.PetMenuDisplay import PetMenuDisplay
from src.pet.PetService import PetService
from src.utils.MenusEnum import MenusEnum
from src.utils.MenusManager import MenusManager
from src.utils.StrUtils import StrUtils
from src.utils.InputUtils import InputUtils


# clase que gestiona el menú de opciones para la gestión de mascotas en la base de datos de MongoDB
class PetManagementMenu:

    # método que muestra el menú de opciones para la gestión de mascotas
    def display_menu(self):

        while True:
            StrUtils.create_header("Opciones de mascotas")
            print("1 - Registrar una mascota")
            print("2 - Listar mascotas")
            print("3 - Buscar una mascota por id")
            print("4 - Actualizar una mascota")
            print("5 - Eliminar una mascota")
            print("6 - Volver al menú de administrador")

            option = InputUtils.int_input("Ingrese una opción: ", 1)
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
            if option == 1:
                self.pet_service.create_pet()
            elif option == 2:
                pets = self.pet_service.get_all_pets()

                PetMenuDisplay().display_pet_header()
                for pet in pets:
                    PetMenuDisplay().display_pet(pet)

            elif option == 3:

                pet_id = input("Ingrese el ID de la mascota a buscar: ")
                pet = self.pet_service.get_pet_by_id(pet_id)
                if pet:
                    PetMenuDisplay().display_pet_header()
                    PetMenuDisplay().display_pet(pet)
                else:
                    print("Mascota no encontrada.")
            elif option == 4:
                pet_id = input("Ingrese el ID de la mascota a actualizar: ")
                pet = self.pet_service.get_pet_by_id(pet_id)
                if not pet:
                    print("Mascota no encontrada")
                    MenusManager(MenusEnum.ADMIN_MENU)
                else:
                    pet_update = {
                        "name": InputUtils.str_input("Ingrese el nuevo nombre de la mascota: "),
                        "species": InputUtils.str_input("Ingrese la especie de la mascota: "),
                        "age": InputUtils.int_input("Ingrese la edad de la mascota: ", 2),
                        "gender": InputUtils.str_input("Ingrese el género de la mascota: "),
                    }
                    self.pet_service.update_pet(pet_id, pet_update)
                    MenusManager(MenusEnum.ADMIN_MENU)
            elif option == 5:
                pet_id = input("Ingrese el ID de la mascota a eliminar: ")

                self.pet_service.delete_pet(pet_id)
                MenusManager(MenusEnum.ADMIN_MENU)

            elif option == 6:
                print("Volviendo al menú de administrador...")
                MenusManager(MenusEnum.ADMIN_MENU)

            else:
                print("Opción no válida. Intente nuevamente.")

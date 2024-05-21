

from utils.InputUtils import InputUtils
from utils.StrUtils import StrUtils
class AdminMenu:
    def __init__(self):
        self.admin_menu = [
            "1 - Opciones de usuarios",
            "2 - Opciones de mascotas",
        ]

    def display_menu(self):
        for item in self.admin_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        self.select_menu(self.option)

    def select_menu(self, option):
        if option == 1:
            self.user_menu()
        elif option == 2:
            print("Opciones de mascotas")
        
    def user_menu(self):
        StrUtils.create_header("Opciones de usuarios")
        print("1 - Registrar un usuario")
        print("2 - Listar usuarios")
        print("3 - Buscar un usuario por email")
        print("4 - Actualizar un usuario")
        print("5 - Eliminar un usuario")
        print("6 - Volver al menú principal")
        option = InputUtils.int_input("Ingrese una opción: ")
    
    def pet_menu(self):
        StrUtils.create_header("Opciones de mascotas")
        print("1 - Registrar una mascota")
        print("2 - Listar mascotas")
        print("3 - Buscar una mascota por nombre")
        print("4 - Actualizar una mascota")
        print("5 - Eliminar una mascota")
        print("6 - Volver al menú principal")
        option = InputUtils.int_input("Ingrese una opción: ")
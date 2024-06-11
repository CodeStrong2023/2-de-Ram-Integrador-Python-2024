from src.User.UserMenuManager import UserMenuManager
from src.utils.InputUtils import InputUtils
from src.utils.StrUtils import StrUtils


# class AdminMenu que contiene las opciones del menú de administrador
class AdminMenu:
    def __init__(self):
        self.admin_menu = [
            "1 - Opciones de usuarios",
            "2 - Opciones de mascotas",
            "3 - Salir",
        ]
        
    # Método para mostrar el menú de administrador
    def display_menu(self):
        StrUtils.create_header("Menú de administrador")
        for item in self.admin_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ", 1)
        self.select_menu(self.option)

    # Método para seleccionar una opción del menú de administrador
    def select_menu(self, option):
        from src.auth.MainMenu import MainMenu
        if option == 1:
            self.user_menu()
        elif option == 2:
            self.pet_menu()
        elif option == 3:
            print("Volviendo al menú principal")

            MainMenu().display_menu()

    # Método para mostrar el menú de usuarios
    def user_menu(self):
        StrUtils.create_header("Opciones de usuarios")
        print("1 - Registrar un usuario")
        print("2 - Listar usuarios")
        print("3 - Buscar un usuario por email")
        print("4 - Actualizar un usuario")
        print("5 - Eliminar un usuario")
        print("6 - Volver al menú de administrador")
        option = InputUtils.int_input("Ingrese una opción: ", 1)
        UserMenuManager().user_admin_menu(option)

    # Método para mostrar el menú de mascotas
    def pet_menu(self):
        StrUtils.create_header("Opciones de mascotas")
        print("1 - Registrar una mascota")
        print("2 - Listar mascotas")
        print("3 - Buscar una mascota por nombre")
        print("4 - Actualizar una mascota")
        print("5 - Eliminar una mascota")
        print("6 - Volver al menú de administrador")
        option = InputUtils.int_input("Ingrese una opción: ", 1)
        # Agregar lógica para las opciones de mascotas

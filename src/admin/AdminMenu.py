from src.User.UserMenuManager import UserMenuManager
from src.utils.InputUtils import InputUtils
from src.utils.StrUtils import StrUtils
# from src.auth.AuthMenu import AuthMenu

class AdminMenu:
    def __init__(self):
        self.admin_menu = [
            "1 - Opciones de usuarios",
            "2 - Opciones de mascotas",
            # "3- Regresar al menú principal"
        ]

    def display_menu(self):
        StrUtils.create_header("Menú de administrador")
        for item in self.admin_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        self.select_menu(self.option)

    # menu_principal = AuthMenu()

    def select_menu(self, option, menu_principal):
        if option == 1:
            self.user_menu()
        elif option == 2:
            print("Opciones de mascotas")
        # elif option == 3:
            # menu_principal.display_menu()


    def user_menu(self):
        StrUtils.create_header("Opciones de usuarios")
        print("1 - Registrar un usuario")
        print("2 - Listar usuarios")
        print("3 - Buscar un usuario por email")
        print("4 - Actualizar un usuario")
        print("5 - Eliminar un usuario")
        print("6 - Volver al menú de administrador")
        option = InputUtils.int_input("Ingrese una opción: ")
        UserMenuManager().user_admin_menu(option)

    def pet_menu(self):
        StrUtils.create_header("Opciones de mascotas")
        print("1 - Registrar una mascota")
        print("2 - Listar mascotas")
        print("3 - Buscar una mascota por nombre")
        print("4 - Actualizar una mascota")
        print("5 - Eliminar una mascota")
        print("6 - Volver al menú principal")
        option = InputUtils.int_input("Ingrese una opción: ")
        # Agregar lógica para las opciones de mascotas

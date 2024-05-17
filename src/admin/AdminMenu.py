from src.User.UserServices import UserServices
from src.utils.InputUtils import InputUtils


class AdminMenu:
    def __init__(self):
        self.admin_menu = [
            "1 - Mostrar listado de usuarios",
            "2 - Mostar listado de mascotas",
            "3 - Editar un usuario"
            "4 - Editar una mascota"
            "5 - Salir"
        ]

    def display_menu(self):
        for item in self.admin_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        self.select_menu(self.option)

    def select_menu(self, option):
        if option == 1:
            print("Mostrar listado de usuarios")
        elif option == 2:
            print("Mostar listado de mascotas")
        elif option == 3:
            print("Editar un usuario")
        elif option == 4:
            print("Editar una mascota")
        elif option == 5:
            print("Salir")

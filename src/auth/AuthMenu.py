from src.utils.InputUtils import InputUtils
from src.User.UserServices import UserServices


class AuthMenu:
    option = 0

    def __init__(self):
        self.auth_menu = [
            "1 - Login",
            "2 - Registro",
            "3 - Salir"
        ]

    def display_menu(self):
        for item in self.auth_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        if self.option == 1:
            print("Ingrese su mail")
        elif self.option == 2:
            register_menu = UserServices()
            register_menu.create_user()
        elif self.option == 3:
            print("Gracias por su visita")

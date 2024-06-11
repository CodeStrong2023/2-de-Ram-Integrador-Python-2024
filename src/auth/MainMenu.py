from src.User.UserServices import UserServices
from src.auth.Login import Login
from src.utils.InputUtils import InputUtils
from src.utils.StrUtils import StrUtils


class MainMenu:
    option = 0

    def display_menu(self):
        StrUtils.create_header("Menú Principal")
        print("1 - Login")
        print("2 - Registro")
        print("3 - Salir")
        print(" ")

        self.option = InputUtils.int_input("Ingrese una opción: ", 1)
        if self.option == 1:
            Login.login()
        elif self.option == 2:
            register_menu = UserServices()
            register_menu.create_user()
        elif self.option == 3:
            print("Gracias por su visita")
        else:
            StrUtils.error_message("Ingrese una opción válida")
            self.display_menu()

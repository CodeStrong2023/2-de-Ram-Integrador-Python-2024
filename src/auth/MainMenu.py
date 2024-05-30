from src.utils.InputUtils import InputUtils
from src.User.UserServices import UserServices
from src.admin.AdminMenu import AdminMenu


class MainMenu:
    option = 0

    def display_menu(self):
        print("1 - Login")
        print("2 - Registro")
        print("3 - Salir")

        self.option = InputUtils.int_input("Ingrese una opción: ")
        if self.option == 1:
            login_menu = AdminMenu()
            login_menu.display_menu()
        elif self.option == 2:
            register_menu = UserServices()
            register_menu.create_user()
        elif self.option == 3:
            print("Gracias por su visita")

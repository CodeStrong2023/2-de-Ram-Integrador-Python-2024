from src.User.UserMenuManager import UserMenuManager
from src.utils.InputUtils import InputUtils
from src.utils.StrUtils import StrUtils
from src.auth.SessionUser import SessionUser



class UserMenu:

    def display_menu(self):
        user = SessionUser.get_user_session()
        StrUtils.create_header(f"Bienvenido {user['name']}")
        print("1- Ver requisitos para adoptar una mascota")
        print("2- Ver mascotas en adopción")
        print("3- Adoptar un mascota responsablemente")
        print("4- Otras opciones del usuario")
        print("5- Salir")

        option = InputUtils.int_input("Ingrese una opción: ", 1)
        UserMenuManager().user_menu(option)

from src.User.UserMenuManager import UserMenuManager
from src.utils.InputUtils import InputUtils
from utils.StrUtils import StrUtils
from auth.SessionUser import SessionUser


class UserMenu:

    def display_menu(self):
        StrUtils.create_header(f"Bienvenido ")
        print("1- Ver requisitos para adoptar una mascota")
        print("2- Ver mascotas en adopción")
        print("3- Adoptar un mascota responsablemente")
        print("4- Otras opciones del usuario")
        print("5- Salir")

        option = InputUtils.int_input("Ingrese una opción: ", 1)
        UserMenuManager().user_menu(option)

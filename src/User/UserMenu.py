from src.User.UserMenuManager import UserMenuManager
from src.utils.InputUtils import InputUtils


class UserMenu:
    def __init__(self):
        self.user_menu = [
            "1- Ver requisitos para adoptar una mascota"
            "2- Ver mascotaes en adopción"
            "3- Adoptar un mascota responsablemente"
            "4- Otras opciones del usuario"
            "5- Regresar al menú principal"
        ]

    def display_menu(self):
        for item in self.user_menu:
            print(item)
        option = InputUtils.int_input("Ingrese una opción: ")
        UserMenuManager().user_menu(option)

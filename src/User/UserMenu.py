from src.User.UserMenuManager import UserMenuManager
from src.User.UserMenusDisplay import UserMenusDisplay
from src.utils.InputUtils import InputUtils
from src.utils.StrUtils import StrUtils
from src.auth.SessionUser import SessionUser



class UserMenu:

    def display_menu(self):
        user = SessionUser.get_user_session()
        StrUtils.create_header(f"Bienvenido {user['name']}")
        print("1- Ver requisitos para adoptar una mascota")
        print("2- Ver mascotas en adopción")
        print("3- Adoptar una mascota responsablemente")
        print("4- Ir al perfil")
        print("5- Regresar al menú principal")

        option = InputUtils.int_input("Ingrese una opción: ", 1)
        UserMenuManager().user_menu(option)

    def user_profile(self):
        StrUtils.create_header("Perfil de usuario")
        UserMenusDisplay().user_profile()
        option = InputUtils.int_input("Ingrese una opción: ", 1)
        UserMenuManager().user_profile_menu(option)
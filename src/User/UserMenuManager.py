from User.UserServices import UserServices
from utils.MenusEnum import MenusEnum
from utils.MenusManager import MenusManager
from User.UserMenusDisplay import UserMenusDisplay
from utils.StrUtils import StrUtils
from utils.InputUtils import InputUtils
from utils.Validations.UserValidations import UserValidations

""" 
Este menú manager se encarga de redirigir a los diferentes menús de la aplicación,
que gestiona los servicios de los usuarios que vamos a ejecutar en dependiendo
si las opciones vienen del menú de usuario o del menú de administrador
"""


class UserMenuManager:

    def user_admin_menu(self, option):
        if option == 1:
            UserServices().create_user()
        elif option == 2:
            users = list(UserServices().get_all_users())
            StrUtils.create_header("Listado de usuarios registrados")
            for user in users:
                UserMenusDisplay().display_user(user)
            MenusManager(MenusEnum.USER_ADMIN_MENU)
        elif option == 3:
            email = InputUtils.email_input("Ingrese el email del usuario: ")
            email_exists = UserValidations().check_mail_exists(email)
            while not email_exists:
                email = InputUtils.email_input("El email ingresado no existe, por favor ingrese un email válido: ")
                email_exists = UserValidations().check_mail_exists(email)
            user = UserServices().get_user_by_email(email)
            StrUtils.create_header("Usuario encontrado")
            UserMenusDisplay().display_user(user)
            MenusManager(MenusEnum.USER_ADMIN_MENU)
        elif option == 4:
            UserServices().update_user()
        elif option == 5:
            UserServices().delete_user()
        elif option == 6:
            MenusManager(MenusEnum.ADMIN_MENU)
        else:
            print("Opción no válida")
            print("")
            MenusManager(MenusEnum.USER_ADMIN_MENU)

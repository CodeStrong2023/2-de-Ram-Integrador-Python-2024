from User.UserServices import UserServices
from utils.MenusEnum import MenusEnum
from utils.MenusManager import MenusManager

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
            UserServices().get_all_users()
        elif option == 3:
            UserServices().get_user_by_email()
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

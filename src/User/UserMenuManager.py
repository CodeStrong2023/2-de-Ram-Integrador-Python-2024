from User.UserServices import UserServices
from utils.MenusEnum import MenusEnum
from utils.MenusManager import MenusManager

class UserMenuManager:

    def user_admin_menu(self, option):
        if option == 1:
            user = UserServices().create_user()
        elif option == 2:
            print("Listar usuarios")
            m = MenusManager(MenusEnum.USER_ADMIN_MENU)
        elif option == 3:
            print("Opciones de veterinarios")
        elif option == 4:
            print("Opciones de citas")
        elif option == 5:
            print("Opciones de servicios")
        elif option == 6:
            print("Opciones de productos")
        else:
            print("Opción no válida")

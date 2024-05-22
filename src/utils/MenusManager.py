from utils.MenusEnum import MenusEnum

""" 
Este menú manager se encarga de redirigir a los diferentes menús de la aplicación,
podemos utilizar en toda la app para las opciones de volver al menú que se encontraba anteriormente
solamente se debe de importar la clase MenusManager y llamar al constructor con el menú que se desea mostrar
también se debe importar el MenusEnum para poder utilizar los menús que tenemos que pasar al constructor de 
MenusManager
"""


class MenusManager:
    def __init__(self, menu):
        from auth.AuthMenu import AuthMenu
        from admin.AdminMenu import AdminMenu
        from User.UserMenu import UserMenu
        from Pet.PetManagementMenu import PetManagementMenu

        if menu == MenusEnum.MAIN_MENU:
            AuthMenu().display_menu()
        elif menu == MenusEnum.USER_MENU:
            UserMenu().user_menu()
        elif menu == MenusEnum.PET_MENU:
            PetManagementMenu().display_menu()
        elif menu == MenusEnum.ADMIN_MENU:
            AdminMenu().display_menu()
        elif menu == MenusEnum.LOGIN_MENU:
            print("Opciones de login")
        elif menu == MenusEnum.USER_ADMIN_MENU:
            AdminMenu().user_menu()
        elif menu == MenusEnum.PET_ADMIN_MENU:
            AdminMenu().pet_menu()

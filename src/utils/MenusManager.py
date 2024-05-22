from utils.MenusEnum import MenusEnum


class MenusManager:
    def __init__(self, menu):
        from auth.AuthMenu import AuthMenu
        from admin.AdminMenu import AdminMenu
        print(menu)
        if menu == MenusEnum.MAIN_MENU:
            m = AuthMenu().display_menu()
        elif menu == MenusEnum.USER_MENU:
            print("Opciones de usuario")
        elif menu == MenusEnum.PET_MENU:
            print("Opciones de mascotas")
        elif menu == MenusEnum.ADMIN_MENU:
            print("Opciones de administrador")
        elif menu == MenusEnum.LOGIN_MENU:
            print("Opciones de login")
        elif menu == MenusEnum.USER_ADMIN_MENU:
            AdminMenu().user_menu()
        elif menu == MenusEnum.PET_ADMIN_MENU:
            print("Opciones de mascotas")

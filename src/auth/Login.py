from src.User.UserServices import UserServices

from src.User.UserMenu import UserMenu
from src.admin.AdminMenu import AdminMenu
from src.utils.InputUtils import InputUtils
from src.auth.SessionUser import SessionUser


class Login:
    user_services = UserServices()
    user_menu = UserMenu()
    admin_menu = AdminMenu()

    @staticmethod
    def login():
        from src.auth.MainMenu import MainMenu

        email = InputUtils.email_input("Ingrese su email: ")
        password = InputUtils.str_input("Ingrese su password: ")
        user = Login.user_services.get_user_by_email(email)

        # Chequeamos que exista el usuario, que el password coincida y que su estatus esté en True
        if not user or user["password"] != password:
            print("Usuario o contraseña no válido")
            return MainMenu().display_menu()

        # Guardamos la sessión de usuario para usar en toda la app
        SessionUser.set_user_session(user)
        
        # Determinamos de acuerdo al rol del usuario lo reenviamos al menú correspondiente
        if user["role"] == "admin":
            Login.admin_menu.display_menu()
        else:
            Login.user_menu.display_menu()

from src.User.UserServices import UserServices
from src.admin.AdminMenu import AdminMenu
from src.User.UserMenu import UserMenu
from src.utils.InputUtils import InputUtils
from src.auth.SessionUser import SessionUser

# Clase que gestiona el login de los usuarios
class Login:
    user_services = UserServices()
    user_menu = UserMenu()
    admin_menu = AdminMenu()

    # Método para iniciar sesión
    @staticmethod
    def login():
        email = InputUtils.email_input("Ingrese su email: ")
        password = InputUtils.str_input("Ingrese su password: ")
        user = Login.user_services.get_user_by_email(email)

        # Chequeamos que exista el usuario, que el password coincida y que su estatus esté en True
        if not user or user["password"] != password or user["status"] == False:
            print("Usuairo o contraseña no válido")
            return Login.login()

        # Guardamos la sessión de usuario para usar en toda la app
        SessionUser.user_session = user

        # Determinamos de acuerdo al rol del usuario lo reenviamos al menú correspondiente
        if user["role"] == "admin":
            Login.admin_menu.display_menu()
        else:
            Login.user_menu.display_menu()

from User.UserServices import get_user_by_email
from utils import InputUtils




class LoginUser:
    def login():
    print("")
    email = InputUtils.email_input("Ingrese su email: ")
    password = InputUtils.str_input("Ingrese su password: ")
    user = get_user_by_email(email)
    if user is not None:
        if email == user.email and password == user.password:
            SessionUser.set_session_user(user)
            if user.role == "admin":
                AdminMenu.get_menu(user.name)
            else:
                UserMenu.get_menu(user.name)
            return
    print("")
    print("Email o contraseña no válida")
    Menu.main_menu()
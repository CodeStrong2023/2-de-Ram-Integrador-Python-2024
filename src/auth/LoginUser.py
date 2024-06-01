from src.User.UserServices import UserServices
from src.utils.InputUtils import InputUtils
from src.admin.AdminMenu import AdminMenu
from src.User.UserMenu import UserMenu

'''
Hay que corregir utiliza clases y métodos que no existen
'''

# class LoginUser:
#     def login(self):
#     print("")
#     email = InputUtils.("Ingrese su email: ")
#     password = InputUtils.str_input("Ingrese su password: ")
#     user = UserServices.get_user_by_email(email)
#     if user is not None:
#         if email == user.email and password == user.password:
#             # SessionUser.set_session_user(user)
#             if user.role == "admin":
#                 AdminMenu.display_menu()
#             else:
#                 UserMenu.display_menu()
#             return
#     print("")
#     print("Email o contraseña no válida")
#     Menu.main_menu()

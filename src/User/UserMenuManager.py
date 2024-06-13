from src.User.UserServices import UserServices
from src.utils.MenusEnum import MenusEnum
from src.utils.MenusManager import MenusManager
from src.User.UserMenusDisplay import UserMenusDisplay
from src.utils.StrUtils import StrUtils
from src.utils.InputUtils import InputUtils
from src.utils.Validations.UserValidations import UserValidations
from src.auth.SessionUser import SessionUser
from src.Pet.PetService import PetService
from src.Pet.PetMenuDisplay import PetMenuDisplay

""" 
Este menú manager se encarga de redirigir a los diferentes menús de la aplicación,
que gestiona los servicios de los usuarios que vamos a ejecutar en dependiendo
si las opciones vienen del menú de usuario o del menú de administrador
"""


class UserMenuManager:
    def __init__(self):
        self.user = SessionUser.get_user_session()

    def user_admin_menu(self, option):
        if option == 1:
            UserServices().create_user()
        elif option == 2:
            users = list(UserServices().get_all_users())
            StrUtils.create_header("Listado de usuarios registrados")
            UserMenusDisplay().display_user_header()
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
            UserMenusDisplay().display_user_header()
            UserMenusDisplay().display_user(user)
            MenusManager(MenusEnum.USER_ADMIN_MENU)
        elif option == 4:
            print("Actualizar usuario")
            user_id = InputUtils.str_input("Ingrese el id del usuario: ")
            user_data_update = {
                "name": InputUtils.str_input("Ingrese el nuevo nombre: "),
                "edad": InputUtils.int_input("Ingrese la nueva edad: ", 2),
                "email": InputUtils.email_input("Ingrese el nuevo email: "),
            }
            UserServices().update_user(user_id, user_data_update)
            print("Usuario actualizado")
            MenusManager(MenusEnum.USER_ADMIN_MENU)
        elif option == 5:
            user_id = InputUtils.str_input("Ingrese el id del usuario: ")
            UserServices().delete_user(user_id)
            print("Usuario eleminado")
            MenusManager(MenusEnum.USER_ADMIN_MENU)
        elif option == 6:
            MenusManager(MenusEnum.ADMIN_MENU)
        else:
            print("Opción no válida")
            print("")
            MenusManager(MenusEnum.USER_ADMIN_MENU)

    def user_menu(self, option):
        if option == 1:
            UserMenusDisplay().user_requirements()
            MenusManager(MenusEnum.USER_MENU)
        elif option == 2:
            print("Animales en adopcion: ")
            pets = list(PetService().get_all_pets())
            PetMenuDisplay().display_pet_header()
            for pet in pets:
                PetMenuDisplay().display_pet(pet)
            MenusManager(MenusEnum.USER_MENU)

        elif option == 3:
            print("Adoptar una mascota")
            pet_id = InputUtils.str_input("Ingrese el ID de la mascota: ")
            UserServices().add_pet_to_user(self.user["id"], pet_id)
            print("Mascota adopada")
        elif option == 4:
            MenusManager(MenusEnum.USER_PROFILE_MENU)
        elif option == 5:
            SessionUser.clear_session_user()
            MenusManager(MenusEnum.MAIN_MENU)

    def user_profile_menu(self, option):

        if option == 1:
            user_data = UserServices().get_user_by_id(self.user["id"])
            UserMenusDisplay().display_user_header()
            UserMenusDisplay().display_user(user_data)
            MenusManager(MenusEnum.USER_PROFILE_MENU)
        elif option == 2:
            new_email = InputUtils.email_input("Ingrese su nuevo email: ")
            UserServices().update_user(self.user["id"], {"email": new_email})
            print("Email actualizado")
            MenusManager(MenusEnum.USER_PROFILE_MENU)
        elif option == 3:
            new_password = InputUtils.str_input("Ingrese su nuevo password")
            UserServices().update_user(self.user["id"], {"password": new_password})
            print("Password actualizado")
            MenusManager(MenusEnum.USER_PROFILE_MENU)

        elif option == 4:
            MenusManager(MenusEnum.USER_MENU)
        else:
            StrUtils.error_message("Ingrese una opción válida")
            option = InputUtils.int_input("Ingrese una opción: ", 1)
            self.user_profile_menu(option)

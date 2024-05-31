from src.User.UserServices import UserServices
from src.utils.MenusEnum import MenusEnum
from src.utils.MenusManager import MenusManager
from src.User.UserMenusDisplay import UserMenusDisplay
from src.utils.StrUtils import StrUtils
from src.utils.InputUtils import InputUtils
from src.utils.Validations.UserValidations import UserValidations

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
        elif option == 2:
            print("Animales en adopcion: ")
        #     Agregar el display del listado de mascotas
        elif option == 3:
            # Modificar para que solicite el método de adopción de mascotas
            # print("Elija el mascota o los mascotaes que desea adoptar: ")
            # PetService.get_all_pets()
            # UserMenuServices.seleccionar_mascota()
            self.display_menu()
        elif option == 4:
            print("Otras opciones del usuario")
            # insertar metodo con menu desplegable para que el usuario gestione su propio usuario
            # Se puede cambiar esta sección por perfil de usuario para que pueda gestionar datos de su cuenta
            self.display_menu()
        elif option == 5:
            MenusManager(MenusEnum.USER_MENU)

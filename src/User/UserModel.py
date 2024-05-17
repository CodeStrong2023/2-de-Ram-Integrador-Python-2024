from src.utils.InputUtils import InputUtils
from src.utils.MenusEnum import MenusEnum


class UserModel:
    def create_user(self):
        user = {
            "name": InputUtils.str_input("Ingrese su nombre: "),
            "email": InputUtils.email_input("Ingrese su email: "),
            "password": InputUtils.str_input("Ingrese su password: "),
            "age": InputUtils.int_input("Ingrese su edad: "),
            "dni": InputUtils.str_input("Ingrese su dni: "),
            "pets": [],
            "status": True
        }
        return user

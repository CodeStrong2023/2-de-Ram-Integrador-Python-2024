from src.utils.InputUtils import InputUtils
from src.utils.MenusEnum import MenusEnum


class UserModel:
    def create_user(self):
        user = {
            "name": InputUtils.str_input("Ingrese su nombre: ", MenusEnum.MAIN_MENU),
            "email": InputUtils.str_input("Ingrese su email: ", MenusEnum.MAIN_MENU),
            "password": InputUtils.str_input("Ingrese su password: ", MenusEnum.MAIN_MENU),
            "age": InputUtils.int_input("Ingrese su edad: "),
            "dni": InputUtils.str_input("Ingrese su dni: ", MenusEnum.MAIN_MENU),
            "pets": [],
            "status": True
        }
        return user

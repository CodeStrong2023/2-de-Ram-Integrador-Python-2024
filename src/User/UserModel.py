from utils.InputUtils import InputUtils


class UserModel:
    def create_user(self):
        user = {
            "name": InputUtils.str_input("Ingrese su nombre: "),
            "email": InputUtils.email_input("Ingrese su email: "),
            "password": InputUtils.str_input("Ingrese su password: "),
            "age": InputUtils.int_input("Ingrese su edad: "),
            "dni": InputUtils.str_input("Ingrese su dni: "),
            "pets": [],
            "status": True,
            "role": "user",
        }

        return user

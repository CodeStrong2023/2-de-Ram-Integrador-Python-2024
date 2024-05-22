from utils.InputUtils import InputUtils
from utils.Validations.UserValidations import UserValidations


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
        # Chequea si el email ya se encuentra registrado
        if UserValidations().check_mail_exists(user["email"]):
            print("El email ya se encuentra registrado")
            return self.create_user()

        return user

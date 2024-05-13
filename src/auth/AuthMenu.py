from src.utils.InputUtils import InputUtils
class auth_menu:
    option = 0
    def __init__(self):
        self.auth_menu = [
            "1 - Login",
            "2 - Register",
            "3 - Exit"
        ]

    def display_menu(self):
        for item in self.auth_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        if self.option == 1:
            print("Ingrese su mail")
        else:
            print("Opción no válida")
            self.option = InputUtils.int_input("Ingrese una opción: ")
    

 
menu = auth_menu().display_menu()
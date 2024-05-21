from utils.InputUtils import InputUtils


class UserMenu:
    def __init__(self):
        self.user_menu = [
            "1- Ver requisitos para adoptar un animal"
            "2- Ver animales en adopción"
            "3- Adoptar un animal responsablemente"
            "4- Regresar al menú principal"
        ]

    def display_menu(self):
        for item in self.user_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        self.select_menu(self.option)

    def select_menu(self, option):
        if option == 1:
            print(" Requisitos para adoptar un animal: ")
            # escribir requisitos para adoptar un animal
        elif option == 2:
            print("Animales en adopcion: ")
            # metodo para insertar y mostrar animales en adopcion con sus caracteristicas
        elif option == 3:
            print("Elija el animal o los animales que desea adoptar: ")
            # metodo para mostrar animales y permitir seleccionar uno o varios
        elif option == 4:
            print("Regresando al menú principal")
            # insertar metodo para regresar al menu principal


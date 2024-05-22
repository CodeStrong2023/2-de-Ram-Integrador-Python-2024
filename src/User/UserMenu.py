from utils.InputUtils import InputUtils

class UserMenu:
    def __init__(self):
        self.user_menu = [
            "1- Ver requisitos para adoptar un animal"
            "2- Ver animales en adopción"
            "3- Adoptar un animal responsablemente"
            "4- Otras opciones del usuario"
            "5- Regresar al menú principal"
        ]

    def display_menu(self):
        for item in self.user_menu:
            print(item)
        self.option = InputUtils.int_input("Ingrese una opción: ")
        self.select_menu(self.option)

    def select_menu(self, option):
        if option == 1:
            print(" Requisitos para adoptar un animal: ")
            print(f'''
                1- Ser mayor de edad.
                2- Adjuntar fotocopias del DNI, del derecho y el reverso. 
                3- Completar formulario de adopción.
                3- Tiempo, compromiso y dedicación. Asegúrate de estar dispuesto a cuidarla y brindarle atención.
                4- Ser una persona o familia responsable que los quiera como a un miembro más, los proteja y cuide.
            ''')
            self.display_menu()
        elif option == 2:
            print("Animales en adopcion: ")
            PetService.get_all_pets()
            self.display_menu()
        elif option == 3:
            print("Elija el animal o los animales que desea adoptar: ")
            PetService.get_all_pets()
            UserMenuServices.seleccionar_mascota()
            self.display_menu()
        elif option == 4:
            print("Otras opciones del usuario")
            # insertar metodo con menu desplegable para que el usuario gestione su propio usuario
            self.display_menu()
        elif option == 5:
            print("Regresando al menú principal")
            # insertar metodo para regresar al menu principal

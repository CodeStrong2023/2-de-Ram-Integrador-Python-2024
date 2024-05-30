class UserMenusDisplay:

    def display_user(self, user):
        header = f"| ID {" " * 20}| NOMBRE {" " * 20}| EMAIL {" " * 20}| EDAD | DNI {" " * 9}| STATUS |"
        print("°" * len(header))
        print(header)
        print("-" * len(header))
        # print(f"| ID {" " * 20}| NOMBRE {" " * 20}| EMAIL {" " * 20}| EDAD {" " * 20}| DNI {" " * 20}| STATUS {" " * 20}| ")
        # print("Nombre: ", user["name"])
        # print("Email: ", user["email"])
        # print("Edad: ", user["age"])
        # print("DNI: ", user["dni"])
        # print("Mascotas: ", user["pets"])
        # print("Estado: ", user["status"])
        print("=" * 20)
        print("")

    def user_requirements(self):
        print(" Requisitos para adoptar una mascota: ")
        print(f'''
                1- Ser mayor de edad.
                2- Adjuntar fotocopias del DNI, del derecho y el reverso. 
                3- Completar formulario de adopción.
                3- Tiempo, compromiso y dedicación. Asegúrate de estar dispuesto a cuidarla y brindarle atención.
                4- Ser una persona o familia responsable que los quiera como a un miembro más, los proteja y cuide.
            ''')

# UserMenusDisplay().display_user({})

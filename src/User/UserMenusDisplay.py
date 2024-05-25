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

UserMenusDisplay().display_user({})
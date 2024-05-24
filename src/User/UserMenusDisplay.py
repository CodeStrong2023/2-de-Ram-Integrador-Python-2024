class UserMenusDisplay:

    def display_user(self, user):
        print("=" * 20)
        print("Nombre: ", user["name"])
        print("Email: ", user["email"])
        print("Edad: ", user["age"])
        print("DNI: ", user["dni"])
        print("Mascotas: ", user["pets"])
        print("Estado: ", user["status"])
        print("=" * 20)
        print("")

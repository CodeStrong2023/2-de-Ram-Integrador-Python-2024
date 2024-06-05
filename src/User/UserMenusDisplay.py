class UserMenusDisplay:
    def display_user_header(self):
        id_header = "ID".center(28, " ")
        name_header = "NOMBRE".center(30, " ")
        email_header = "EMAIL".center(30, " ")
        age_header = "EDAD".center(6, " ")
        dni_header = "DNI".center(10, " ")
        status_header = "STATUS".center(8, " ")
        header = f"|{id_header}|{name_header}|{email_header}|{age_header}|{dni_header}|{status_header}|"
        print("°" * len(header))
        print(header)
        print("°" * len(header))

    def display_user(self, user):
        print(
            f"| {str(user['_id']).ljust(26)} "
            f"| {str(user['name']).ljust(28)} "
            f"| {str(user['email']).ljust(28)} "
            f"| {str(user['age']).ljust(4)} "
            f"| {str(user['dni']).ljust(8)} "
            f"| {str(user['status']).ljust(6)} |")

        print("")

    def user_requirements(self):
        print(" Requisitos para adoptar una mascota: ")
        print("1- Ser mayor de edad.")
        print("2- Adjuntar fotocopias del DNI, del derecho y el reverso.")
        print("3- Completar formulario de adopción.")
        print("4- Tiempo, compromiso y dedicación. Asegúrate de estar dispuesto a cuidarla y brindarle atención.")
        print("5- Ser una persona o familia responsable que los quiera como a un miembro más, los proteja y cuide.")


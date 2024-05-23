class MyAdmin:

    howMany = 0

    def __init__(self, name, lastname, user, password, age, dni, birth_date):
        self.name = name  # nombre
        self.lastname = lastname  # apellido
        self.user = user  # usuario
        self.password = password  # contraseña
        self.age = age  # edad
        self.dni = dni  # Documento nacional de identidad
        self.birth_date = birth_date  # fecha de nacimiento
        MyAdmin.howMany += 1
        _id_admin = MyAdmin.howMany

    def __str__(self):
        return f'''
        Admin:
        Nombre: {self.name}
        Apellido: {self.lastname}
        Usuario: {self.user}
        Contraseña: {self.password}
        Edad: {self.age}
        DNI: {self.dni}
        Fecha de Nacimiento: {self.birth_date}
    '''

class UserModel:
    def create_user(self, name, email, password, age, dni):
        user = {
            "name": name,
            "email": email,
            "password": password,
            "age": age,
            "dni": dni,
            "pets": [],
            "status": True
            }
        return user



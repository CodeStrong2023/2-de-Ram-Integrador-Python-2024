from config.ConnectMongo import ConnectMongo


class UserValidations:
    def __init__(self):
        self.connection = ConnectMongo()
        self.user_collection = self.connection.db.get_collection("users")

    def validate_admin_role(self, user):
        # Verificar si el usuario tiene el rol de administrador
        if user.get("role") == "admin":
            return True
        else:
            return False
    
    def check_mail_exists(self, email):
        user = self.user_collection.find_one({"email": email})
        if user:
            return True
        else:
            return False
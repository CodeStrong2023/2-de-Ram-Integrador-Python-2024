class User_validations:

    def validate_admin_role(self, user):
        # Verificar si el usuario tiene el rol de administrador
        if user.get("role") == "admin":
            return True
        else:
            return False
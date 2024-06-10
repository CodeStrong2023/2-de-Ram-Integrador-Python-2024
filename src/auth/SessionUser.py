class SessionUser:
    user_session = None

    @staticmethod
    def set_user_session(user):
        user = {
            "id": user["_id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "pets": user["pets"],
        }
        SessionUser.user_session = user

    @staticmethod
    def clear_session_user():
        SessionUser.user_session = None

    @staticmethod
    def get_user_session():
        return SessionUser.user_session

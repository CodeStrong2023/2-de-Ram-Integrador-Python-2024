user_session = None


class SessionUser:

    @staticmethod
    def set_user_session(user):
        user = {
            "id": user["_id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "pets": user["pets"],
        }
        global user_session
        user_session = user

    @staticmethod
    def clear_session_user():
        global user_session
        user_session = None

    @staticmethod
    def get_user_session():
        global user_session
        return user_session

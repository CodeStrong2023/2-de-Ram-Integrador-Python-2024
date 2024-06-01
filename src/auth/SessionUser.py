class SessionUser:
    user_session = None

    def __init__(self, id, user_name, role, email):
        self.user_session = {
            "id": id,
            "name": user_name,
            "role": role,
            "email": email
        }

    # @property
    # def get_user_session(self):
    #     user_session = {
    #         "name": self._user_name,
    #         "role": self._role,
    #         "email": self._email
    #     }
    #     return user_session

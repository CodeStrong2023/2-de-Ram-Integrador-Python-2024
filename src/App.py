from src.User.UserServices import *

class App:

    def __init__(self):
        self.user_services = UserServices()
        self.user_services.create_user()

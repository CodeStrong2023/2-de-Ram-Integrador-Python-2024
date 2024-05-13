from src.User.UserServices import *
from src.auth.AuthMenu import auth_menu

class App:

    def __init__(self):
        self.auth_menu = auth_menu()
        self.auth_menu.display_menu()

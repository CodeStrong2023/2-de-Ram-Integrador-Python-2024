from auth.AuthMenu import AuthMenu



class App:
    def __init__(self):
        self.auth_menu = AuthMenu()
        self.auth_menu.display_menu()

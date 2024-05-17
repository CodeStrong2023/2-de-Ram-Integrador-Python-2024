from src.utils.MenusEnum import MenusEnum
from src.auth.AuthMenu import AuthMenu


class MenuManager:
    _last_menu = None

    def __init__(self, last_menu):
        self._last_menu = last_menu

    @staticmethod
    def select_menu(self, menu):
        if menu == MenusEnum.MAIN_MENU:
            AuthMenu().display_menu()

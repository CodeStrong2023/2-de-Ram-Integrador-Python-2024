import unittest
from unittest.mock import patch
from src.User.UserMenuManager import UserMenuManager
from src.admin.AdminMenu import AdminMenu
from src.utils.InputUtils import InputUtils
from src.utils.StrUtils import StrUtils



class TestAdminMenu(unittest.TestCase):

    @patch.object(StrUtils, 'create_header')
    @patch.object(InputUtils, 'int_input')
    def test_display_menu(self, mock_int_input, mock_create_header):
        mock_int_input.return_value = 3
        admin_menu = AdminMenu()

        with patch.object(admin_menu, 'select_menu') as mock_select_menu:
            admin_menu.display_menu()
            mock_select_menu.assert_called_once_with(3)

        mock_create_header.assert_called_once_with("Menú de administrador")
        mock_int_input.assert_called_once_with("Ingrese una opción: ", 1)

    @patch('src.admin.AdminMenu.AdminMenu.user_menu')
    @patch('src.admin.AdminMenu.AdminMenu.pet_menu')
    @patch('src.auth.MainMenu.MainMenu.display_menu')
    def test_select_menu(self, mock_main_menu_display, mock_pet_menu, mock_user_menu):
        from src.admin.AdminMenu import AdminMenu

        admin_menu = AdminMenu()

        admin_menu.select_menu(1)
        mock_user_menu.assert_called_once()
        mock_pet_menu.assert_not_called()
        mock_main_menu_display.assert_not_called()

        mock_user_menu.reset_mock()
        admin_menu.select_menu(2)
        mock_pet_menu.assert_called_once()
        mock_user_menu.assert_not_called()
        mock_main_menu_display.assert_not_called()

        mock_pet_menu.reset_mock()
        admin_menu.select_menu(3)
        mock_main_menu_display.assert_called_once()
        mock_user_menu.assert_not_called()
        mock_pet_menu.assert_not_called()

    @patch.object(StrUtils, 'create_header')
    @patch.object(InputUtils, 'int_input')
    @patch.object(UserMenuManager, 'user_admin_menu')
    def test_user_menu(self, mock_user_admin_menu, mock_int_input, mock_create_header):
        mock_int_input.return_value = 1
        admin_menu = AdminMenu()

        admin_menu.user_menu()

        mock_create_header.assert_called_once_with("Opciones de usuarios")
        mock_int_input.assert_called_once_with("Ingrese una opción: ", 1)
        mock_user_admin_menu.assert_called_once_with(1)

    @patch.object(StrUtils, 'create_header')
    @patch.object(InputUtils, 'int_input')
    def test_pet_menu(self, mock_int_input, mock_create_header):
        mock_int_input.return_value = 1
        admin_menu = AdminMenu()

        with patch.object(admin_menu, 'select_menu') as mock_select_menu:
            admin_menu.pet_menu()

        mock_create_header.assert_called_once_with("Opciones de mascotas")
        mock_int_input.assert_called_once_with("Ingrese una opción: ", 1)


if __name__ == '__main__':
    unittest.main()

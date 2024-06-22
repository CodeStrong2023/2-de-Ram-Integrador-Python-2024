import unittest
from unittest.mock import patch
from src.pet.PetManagementMenu import PetManagementMenu
from src.pet.PetService import PetService

class TestPetManagementMenu(unittest.TestCase):

    @patch('builtins.input', side_effect=["1", "Bobtail", "Cat", "Siamese", "2", "Male", "Gray","0"])
    def test_menu_option_1(self, mock_input):
        menu = PetManagementMenu()
        menu.pet_service = PetService()  # Mock or create a fake PetService for testing
        menu.display_menu()
        # Verificar que el método create_pet se llamó correctamente
        self.assertTrue(menu.pet_service.create_pet.called)

        # Obtener la última llamada al método create_pet y verificar los argumentos pasados
        create_pet_call_args = menu.pet_service.create_pet.call_args_list[-1][0]
        self.assertEqual(create_pet_call_args[0], "Bobtail")  # Nombre
        self.assertEqual(create_pet_call_args[1], "Cat")  # Especie
        self.assertEqual(create_pet_call_args[2], "Siamese")  # Raza
        self.assertEqual(create_pet_call_args[3], 2)  # Edad
        self.assertEqual(create_pet_call_args[4], "Male")  # Género
        self.assertEqual(create_pet_call_args[5], "Gray")  # Color

    @patch('builtins.input', side_effect=["2"])
    def test_menu_option_2(self, mock_input):
        menu = PetManagementMenu()
        menu.pet_service = PetService()  # Mock or create a fake PetService for testing
        menu.display_menu()
        

if __name__ == '__main__':
    unittest.main()
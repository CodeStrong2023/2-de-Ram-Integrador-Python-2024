import unittest
from unittest.mock import MagicMock, patch

from src.config.ConnectMongo import ConnectMongo
from src.Pet.PetModel import PetModel

from src.Pet.PetService import PetService

class TestPetService(unittest.TestCase):


    # Crear un mock para la conexión a la base de datos
    mock_db_connection = MagicMock()

    # Configurar el mock para simular la conexión a la base de datos
    mock_db_connection.return_value = 'Conexión exitosa'  # Puedes personalizar el retorno según tus necesidades

    # Crear un mock para la colección de mascotas
    mock_pet_collection = MagicMock()

    # Configurar el mock para simular el método insert_one de la colección
    mock_insert_one = MagicMock()
    mock_pet_collection.insert_one = mock_insert_one

    # Asignar el mock de la colección de mascotas a la conexión simulada
    mock_db_connection.pet_collection = mock_pet_collection

    @patch('src.config.ConnectMongo.ConnectMongo')
    def setUp(self, mock_mongo):
        self.connect_mock = MagicMock()
        self.connect_mock.find.return_value = [{"name": "Mascota", "age": 4}]
        mock_mongo.return_value = self.connect_mock
        self.pet_service_instance = PetService()

    def test_create_pet(self):
        self.pet_service_instance.pet_collection = self.connect_mock
        PetModel.create_pet = MagicMock(return_value={"name": "Prueba", "age": 2})

        self.pet_service_instance.create_pet()
        self.assertTrue(len(self.pet_service_instance.pet_collection.insert_one.call_args) > 0)

    from src.config.ConnectMongo import ConnectMongo

    class PetService:
        def __init__(self):
            # Crear una instancia de ConnectMongo para interactuar con la base de datos
            self.db_connection = ConnectMongo()
            self.pet_collection = self.db_connection.get_collection_db("pet_collection")

        # Método para guardar una nueva mascota en la base de datos
        def save_pet(self, pet_data):
            # Utilizar el método insert_one de la colección para insertar la mascota
            inserted_pet = self.pet_collection.insert_one(pet_data)
            return inserted_pet.inserted_id  # Devolver el ID de la mascota insertada

    # En tu código de prueba (TestPetService), puedes utilizar el siguiente fragmento para probar la inserción de una mascota:

    def test_save_pet(self):
        # Crear una instancia de PetService
        pet_service_instance = PetService()

        # Datos de la nueva mascota a guardar
        new_pet_data = {
            "name": "Nueva Mascota",
            "age": 5
        }

        # Llamar al método save_pet del servicio de mascotas
        inserted_id = pet_service_instance.save_pet(new_pet_data)

        # Verificar que se haya devuelto un ID de mascota insertado
        self.assertIsNotNone(inserted_id)

    def test_get_all_pets(self):
        self.pet_service_instance.pet_collection = self.connect_mock
        pets = self.pet_service_instance.get_all_pets()
        self.assertEqual(len(pets), 1)

    def test_get_pet_by_id(self):
        self.pet_service_instance.pet_collection = self.connect_mock
        pet_id = 1234
        pet = self.pet_service_instance.get_pet_by_id(pet_id)
        self.assertEqual(pet["_id"], pet_id)

    def test_get_pet_by_id(self):
        self.pet_service_instance.pet_collection = self.connect_mock

        # Crear un diccionario con el id de la mascota y otros datos simulados
        pet_data = {
            "_id": 1234,
            "name": "Prueba",
            "age": 2
        }

        # Configurar el retorno del método find_one del mock para devolver los datos simulados
        self.connect_mock.find_one.return_value = pet_data

        # Llamar al método get_pet_by_id con el id de la mascota
        retrieved_pet = self.pet_service_instance.get_pet_by_id(pet_data["_id"])

        # Comparar el id del objeto devuelto con el id esperado
        self.assertEqual(retrieved_pet["_id"], pet_data["_id"])

    @patch('src.config.ConnectMongo.ConnectMongo')
    def test_save_pet(self, mock_mongo):
        mock_mongo.return_value = self.connect_mock
        self.pet_service_instance.pet_collection = self.connect_mock
        pet_data = {"name": "Thor",
            "species": "Perro",
            "breed": "Pastor Belga",
            "age": 3,
            "gender": "Macho",
            "color": "Negro",
            "hair": "Largo",
            "size": "Grande",
            "coat": "Largo",
            "energy": "Muy energico",
            "sociability": "Muy sociable"}
        self.pet_service_instance.save_pet(pet_data)
        self.assertTrue(len(self.pet_service_instance.pet_collection.insert_one.call_args) > 0)

    @patch('src.config.ConnectMongo.ConnectMongo')
    def test_save_pet(self, mock_mongo):
        mock_mongo.return_value = self.connect_mock
        self.pet_service_instance.pet_collection = self.connect_mock

        # Datos de la nueva mascota a guardar
        new_pet_data = {
            "name": "Nueva Mascota",
            "age": 5
        }

        # Crear una instancia de la mascota a partir de los datos
        new_pet = PetModel(new_pet_data)

        # Llamar al método save_pet del servicio de mascotas
        self.pet_service_instance.save_pet(new_pet.to_dict())

        # Verificar que se llamó al método insert_one de la colección
        self.assertTrue(len(self.pet_service_instance.pet_collection.insert_one.call_args) > 0)

    def test_save_pet(self):
        self.pet_service_instance.pet_collection = self.connect_mock
        pet_data = {"name": "Prueba", "age": 2}

        # Simula la inserción de la mascota en la base de datos
        self.connect_mock.insert_one.return_value.inserted_id = 1234

        # Llama al método para guardar la mascota
        self.pet_service_instance.save_pet(pet_data)

        # Verifica que se haya llamado al método insert_one con los datos correctos
        self.connect_mock.insert_one.assert_called_once_with(pet_data)

    @patch('src.config.ConnectMongo.ConnectMongo')
    def test_update_pet(self, mock_mongo):
        mock_mongo.return_value = self.connect_mock
        self.pet_service_instance.pet_collection = self.connect_mock
        pet_id = 1234
        pet_data = {"name": "Prueba cambiada", "age": 3}
        self.pet_service_instance.update_pet(pet_id, pet_data)
        self.assertTrue(len(self.pet_service_instance.pet_collection.update_one.call_args) > 0)

if __name__ == '__main__':
    unittest.main()
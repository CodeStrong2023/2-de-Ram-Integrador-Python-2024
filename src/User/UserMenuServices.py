from src.config.ConnectMongo import ConnectMongo
from src.utils.InputUtils import InputUtils


class UserMenuServices:
    def __init__(self):
        self.connection = ConnectMongo()

    def seleccionar_mascota(self, pet_id):
        id_select = InputUtils.int_input("Ingrese ID de la mascota a adoptar: ")
        '''Ciclar para comparar y utilizar un condicional para encontrar el id coincidente,
        en caso de coincidir modificar la base de datos, si no coincide mostrar un mensaje
        '''

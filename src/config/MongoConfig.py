from pymongo import MongoClient


class MongoConfig:


    def __init__(self, host='localhost', port=27017, db_name="adoptame"):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.db = self.connect()

    def connect(self):
        try:
            self.client = MongoClient(host=self.host, port=self.port, serverSelectionTimeoutMS=2000)
            self.client.server_info()  # Intentar obtener información del servidor para verificar la conexión
            if self.db_name:
                self.db = self.client[self.db_name]

            else:
                self.db = self.client
            print("Conexión exitosa a MongoDB")

            return self.db
        except Exception as e:
            print(f"Error al conectar a MongoDB: {e}")
            return None

    def create_collection(self, collection_name):
        collections = self.db.list_collection_names()
        for name in collections:
            if name == collection_name:
                return False
            else:
                self.db.create_collection(collection_name)



from config.MongoConfig import MongoConfig 

class App:
    mongoConfig = MongoConfig()
    def __init__ (self):
        self.mongoConfig.connect()
        self.mongoConfig.create_collection("prueba")
        self.mongoConfig.create_collection("prueba2")

        
    
    
        
        
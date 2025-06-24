import configparser
from configparser import ConfigParser

class ConfigManager(ConfigParser):
    __file_path: str
    
    def __init__(self, file_path: str):
        super().__init__()
        
        self.read(file_path)
        self.__file_path = file_path
    
    def save(self):
        
        with open(self.__file_path, 'w') as config_file:
            self.write(config_file)
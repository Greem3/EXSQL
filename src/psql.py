import subprocess
from src.configmanager import ConfigManager

class Psql:
    
    __user: str
    __database: str
    __server: str
    __port: int
    
    def __init__(self, *, user: str = '', database: str = 'postgres', server: str = 'localhost', port: int = 5432, config_file: ConfigManager|None = None):
        
        if config_file:
            self.__user = config_file['login']['user']
            self.__server = config_file["login"]["server"]
            self.__port = config_file.getint("login", "port")
            self.__database = database
        
        self.__user = user
        self.__database = database
        self.__server = server
        self.__port = port
    
    def move(self, to_database: str):
        self.__database = to_database
    
    def execute(self, query: str, **args):
        return subprocess.run(f'psql -h {self.__server} -U {self.__user} -p {self.__port} -d {self.__database} -c "{query}"', **args)
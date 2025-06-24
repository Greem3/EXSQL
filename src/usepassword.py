import os
from src.configmanager import ConfigManager
from functools import wraps

def use_password(config_file: ConfigManager):
    
    def decorator(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            os.environ["PGPASSWORD"] = config_file['login']['password']
        
            result = func(*args, **kwargs)
            
            del os.environ["PGPASSWORD"]
            
            return result
        
        return wrapper
    
    return decorator
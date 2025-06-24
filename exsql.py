import typer
from typer import Typer
import subprocess
import os
from src.configmanager import ConfigManager
from src.usepassword import use_password
from src.psql import Psql
from common.schemas import *

if not os.path.exists('config.ini'):
    
    with open('config.ini.template', 'r') as template:
        
        with open('config.ini', 'w') as real:
            real.write(template.read())

config = ConfigManager('config.ini')

app = Typer()

@app.command()
def login(u: str, p: str, s: str = 'localhost', port: int = 5432):
    '''
    Saves your login into config.init to use in others commands
    
    Args:
        u: Server User.
        p: User password.
        s: Server (default localhost),
        port: Connection Port (default 5432)
    
    Returns:
        None
    
    Raises:
        I don't know
    '''
    
    configs: list[tuple[str, str]] = [
        ('user', u),
        ('password', p),
        ('server', s),
        ('port', str(port))
    ]
    
    for values in configs:
        config.set('login', *values)
    
    config.save()

@app.command()
@use_password(config)
def init(database_name: str):
    '''
    Create a new database with the base configuration needed for exsql
    
    Args:
        database_name: Name of the new database.
    
    Returns:
        None
    
    Raises:
        I don't know
    '''
    
    psql = Psql(config_file=config)
    
    create_result = psql.execute(f"CREATE DATABASE {database_name};", shell=True)
    
    psql.move(database_name)
    
    schema_result = add_default_schema(psql)
    
    print(create_result, schema_result)

@app.command()
@use_password(config)
def transfer(database_name: str):
    '''
    Adds base configuration to an already created database
    
    Args:
        database_name: Name of the database.
    
    Returns:
        None
    
    Raises:
        I don't know
    '''
    
    psql = Psql(config_file=config, database=database_name)
    
    schema_result = add_default_schema(psql)
    
    print(schema_result)

if __name__ == '__main__':
    app()
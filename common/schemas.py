from src.psql import Psql

def add_default_schema(psql: Psql):
    
    return psql.execute(f"CREATE SCHEMA exsql_meta;", shell=True)
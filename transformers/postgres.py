import lark
from lark import Lark, Transformer, v_args, Token, Tree

@v_args(inline=True)
class PostgresTransformer(Transformer):
    
    def start(self, *statements):
        
        return "\n\n".join(statements)
    
    def OBJECT_NAME(self, token: Token):
        return str(token)
    
    def CREATE_QUERY(self, token: Token):
        return str(token)
    
    def UPDATE_QUERY(self, token: Token):
        return str(token)
    
    def DROP_QUERY(self, token: Token):
        return str(token)
    
    def TYPE(self, token: Token):
        return str(token)
    
    def EDIT_QUERY(self, token: Token):
        return str(token)
    
    def statement(self, stmt):
        return stmt
    
    def table_stmt(self, stmt):
        return stmt
    
    def create_table(self, table_name, field_block=None, subtype=None):
        
        sql = f'CREATE TABLE {table_name}'
        
        if field_block:
            fields_sql = ',\n'.join(field_block)
            
            sql += f'(\n{fields_sql}\n)'
        
        if subtype:
            pass
        
        sql += ";"
        
        return sql
    
    def drop_table(self, table_name):
        return f"DROP TABLE {table_name}"
    
    def subtype(self, parent_name):
        return str(parent_name)
    
    def field_block(self, *fields):
        return fields
    
    def field(self, field_name, field_type):
        sql_type = 'INT' if field_type == 'int' else 'TEXT'
        return f"{field_name} {sql_type}"
import lark
from lark import Lark, Transformer, v_args
from transformers.postgres import PostgresTransformer
import os

parser = Lark.open('grammars/main.lark', start="start")

#file_to_open = input()

with open(f"testFile.exsql") as f:
    source_code = f.read()

tree = parser.parse(source_code)
sql_output = PostgresTransformer().transform(tree)

print(sql_output)
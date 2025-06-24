
# What is EXSQL about?

**Enhanced and eXtended Structured Query Language** (**EXSQL**) is actually a transpiler (like JSX),
which seeks to **improve** SQL by simplifying tasks and improving the **syntax**, such as inheritance in databases,
making it a rather complicated and exhausting task, instead, thanks to EXSQL we could do something like “SUBTYPE OF”
in a CREATE TABLE and it would generate all the necessary **logic** for the database but we would be using EXSQL to do everything.

## How to start a database with exsql

At this time EXSQL only supports dessert databases and starting a database with exsql configuration is useless besides having a useless schema, but here is how:

<hr/>

You have to run the command:
```bash
python exsql.py login <server_user_name> <password_of_user>
```
This is so that the program saves your login in the config.ini

<hr/>

And now create a new database with:
```bash
python exsql.py init <database_name>
```

Or load the default EXSQL configuration into an already created database:
```bash
python exsql.py transfer <database_name>
```
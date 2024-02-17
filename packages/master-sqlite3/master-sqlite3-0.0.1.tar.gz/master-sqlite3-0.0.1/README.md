# Master SQLite3
The Master SQLite3 library is a powerful and easy-to-use tool that significantly simplifies interaction with SQLite databases in Python.

# How to import?
from Master_SQLite3 import *

# How to create the instance?
bank = MasterSQLite(name='database',path='./')

# How to create the database?
bank.to_create()

# How to connect?
bank.to_connect()

# How to create a table?
bank.setTable(tabela=['id',Rule.primary_key],tabela_2=['id',Rule.primary_key])

bank.setTable(tabela=['id','INTEGER PRIMARY KEY'],tabela_2=['id','INTEGER PRIMARY KEY'])

# How to create a column within the table?
bank.setColumn(table='my_table',column=['my_column',Rule.text])

bank.setColumn(table='my_table',column=['my_column','TEXT'])

# How to create delete a table?
bank.deleteTable(table='my_table')

# How to get all values within the database?
bank.get(table='my_table')

# How to get a specific value?
bank.get_single_value(value='my_value',table='my_table',column='my_column')

# How to obtain complete data?
bank.get_full_data(table='my_table',unique='my_unique')
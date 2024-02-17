import sqlite3

class Rule:
    """Ready parameters
    primary_key = 'PRIMARY KEY'
    integer = 'INTEGER'
    text = 'TEXT'
    """
    primary_key = 'INTEGER PRIMARY KEY'
    integer = 'INTEGER'
    text = 'TEXT'
    real = 'REAL'
    blob = 'BLOB'
    not_null = 'NOT NULL'
    unique = 'UNIQUE'       

# MASTER CREATE OBJECT
class MasterSQLite():
    """c:/path/name

        PATH = PLACE WHERE YOU WILL BE SAVED

        NAME = FILE NAME WITHOUT EXTENSION
    """
    def __init__(self,name:str,path:str='./'):
        self.name = name
        self.path = path

    # CREATE
    def to_create(self):
        sqlite3.connect(f'{self.path}/{self.name}.db')
    
    # CREATE AND CONNECT
    def to_connect(self):
        self.conn = sqlite3.connect(f'{self.path}/{self.name}.db')
        self.cursor = self.conn.cursor()

    # DISCONNECT
    def to_disconnect(self):
        self.conn.close()

    # COMMIT
    def to_commit(self):
        self.conn.commit()

    # EXECUTE
    def execute(self,code):
        self.cursor.execute(code)

    # CREATE TABLE
    def setTable(self, **tables:str):
        """ args = [column , rule]
        column: str
        rule: object Rule or str

        Exemple: table = ["car" , Rule.text]

        Exemple Two: table = ["color" , "TEXT"]
        """
        cache = []
        n = 0
        for table in tables:
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table} (
                              {tables[table][0]} {tables[table][1]}
            );""")
            n = n + 1
            cache.append(table)

    # CREATE COLUMN
    def setColumn(self,table:str,column:list):
        """table = name table, column = [name column, rule column]
           
           Exemple: table = "my_table", column = ["my_column" , Rule.integer]

           Exemple Two: table = "my_table", column = ["my_column" , "INTEGER"]
        """

        self.cursor.execute(f"""ALTER TABLE {table} ADD COLUMN {column[0]} {column[1]}""")

    # DELETE TABLE
    def deleteTable(self,table:str):
        """Delete for table
        """
        self.cursor.execute(f"""DROP TABLE IF EXISTS {table}""")

    # GET ALL VALUES
    def get(self,table:str):
        """get all values"""
        self.cursor.execute(f"""SELECT * FROM {table}""")

        return self.cursor.fetchall()

    # GET SPECIFIC VALUE
    def get_single_value(self,value:str,table:str,column:str):
        self.cursor.execute(f"""SELECT * FROM {table} WHERE {column} LIKE ?""", ('%' + value + '%',))

        return self.cursor.fetchall()

    # GET COMPLETE DATA
    def get_full_data(self,table:str,unique:str):
        """Needs to receive a unique value within a table"""
        self.cursor.execute(f"""SELECT * FROM {table} WHERE id LIKE {unique}""")

        return self.cursor.fetchall()

   

    
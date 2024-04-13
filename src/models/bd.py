from psycopg2 import connect

class Database():
    def __init__(
        self,
        database:str = "ydgyztao",
        host:str = "isabelle.db.elephantsql.com",
        user:str = "ydgyztao",
        password:str = "6NrXuPaXhvTxfhXLd3xbXtb_VAaqtL3t",
        port:str = "5432"):
        
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        
        self.is_connect = False
        
    def connect(self):
        if self.is_connect == False:
            self.conn = connect(database=self.database,host=self.host,user=self.user,password=self.password, port=self.port)
            self.is_connect = True
            self.cursor = self.conn.cursor()
    
    def disconnect(self):
        if self.is_connect == True:
            self.cursor.close()
            self.conn.close()
            self.is_connect = False
            self.cursor = None
            self.conn = None
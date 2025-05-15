import mysql.connector
from mysql.connector import errorcode, Error

class MySQL:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host="db",
                port="3306",
                database="non_verbal_reasoning",
                user="root",
                password="P@ssW0rd"
        )

        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
                host="db",
                port="3306",
                database="non_verbal_reasoning",
                user="root",
                password="P@ssW0rd"
        )

    def close_connection(self):
        self.conn.close()
    
    def create_cursor(self):
        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def close_cursor(self):
        self.curr.close()

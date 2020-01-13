import pymysql
import hashlib

#db = pymysql.connect("database_host","username","password","database_name")

class MyDataBase(object):
    
    def __init__(self, database_host, server_username, server_password, database_name):
        self.conn=pymysql.connect(database_host, server_username, server_password, database_name)
        
    def __del__(self):
        self.conn.close() 
    
    def insert_query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            #return cursor.fetchall()
     
    def select_query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()
    


 







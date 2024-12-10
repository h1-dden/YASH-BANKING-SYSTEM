
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

con = None
cursor = None

class DbService:

    """Creates  a connection to the database and provides methods for closing the connection."""

    def __init__(self):
        
        """Initializes connection to database"""

        global con,cursor
        con = pymysql.connect(host=os.getenv("DB_HOST") ,user=os.getenv("DB_USER") ,
                              password=os.getenv("DB_PASSWORD") , db=os.getenv("DB_SCHEMA"))
        cursor = con.cursor()
    
    def cleanup(self):

        """Closes connection to the database"""
        
        cursor.close()
        con.close()
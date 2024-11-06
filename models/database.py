
import pymysql
from constants import const

con = None
cursor = None

class DbService:

    """Creates  a connection to the database and provides methods for closing the connection."""

    def __init__(self):
        
        """Initializes connection to database"""

        global con,cursor
        con = pymysql.connect(host=const.HOST ,user=const.USER ,password=const.PASSWORD , db=const.DATABASE)
        cursor = con.cursor()
    
    def cleanup(self):

        """Closees connection to the database"""
        
        cursor.close()
        con.close()
# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
from app import models
  
# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'cryptotracket'
  
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    try :
        return create_engine(
            url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database
            ), echo=True, future=True
        )
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
        return 0
  
  
def createTable(engine) :
    try:
        models.declarative().metadata.create_all(engine)
        return 1
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
        return 0
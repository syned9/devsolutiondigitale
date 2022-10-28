# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
import os
from sqlalchemy import create_engine
from app import models
from flask import current_app as flask_app
    
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    try :
        return create_engine(
            url=flask_app.config['SQLALCHEMY_DATABASE_URI'], echo=True, future=True
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
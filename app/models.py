from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    symbole = Column(String(100))
    prix = Column(Float)
    quantite = Column(Integer)
    date = Column(DateTime)

class Valorisation(Base):
    __tablename__ = "valorisation"
    id = Column(Integer, primary_key = True)
    valeur = Column(Float)
    date = Column(DateTime)

def declarative():
    return Base

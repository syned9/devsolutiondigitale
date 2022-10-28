from flask import url_for, redirect
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from app import db
from .models import Transaction
engine = db.get_connection()

def transactionAdd(form):
    try:
        crypto=form['crypto'].split(';')
        with Session(engine) as session:
            transaction = Transaction(
                name=crypto[0],
                symbole=crypto[2],
                prix=form['prix'],
                quantite=form['quantite'],
                date=datetime.now()
            )

            session.add(transaction)
            session.commit()
            return 1
    except Exception as ex:
        print("Insert could not be made due to the following error: \n", ex)
        return 0


def transactionList():
    try:
        session = Session(engine)
        stmt = select(Transaction)
        return session.scalars(stmt)
    except Exception as ex:
        print("Select could not be made due to the following error: \n", ex)
        return 0

def getTransaction(id):
    try:
        session = Session(engine)
        stmt = select(Transaction).where(Transaction.id == id)
        return session.scalar(stmt)
    except Exception as ex:
        print("Select with id could not be made due to the following error: \n", ex)
        return 0

def getTransactionName(name):
    try:
        session = Session(engine)
        stmt = select(Transaction).where(Transaction.name == name)
        return session.scalar(stmt)
    except Exception as ex:
        print("Select with name could not be made due to the following error: \n", ex)
        return 0

def delTransaction(id):
    try :
        session = Session(engine)
        transaction = session.get(Transaction, id)
        session.delete(transaction)
        session.commit()
        return redirect(url_for('home'))
    except Exception as ex:
        print("Delete could not be made due to the following error: \n", ex)
        return ex
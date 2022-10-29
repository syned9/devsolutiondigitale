from flask import url_for, redirect
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from app import db
from .models import Transaction
engine = db.get_connection()


"""
It takes a form as an argument, and then it tries to add a transaction to the database.

:param form: a dictionary containing the following keys:
:return: The return value is the result of the last expression evaluated.
"""
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


"""
It creates a session, creates a statement, and returns the results of the statement
:return: A list of all the transactions in the database.
"""
def transactionList():
    try:
        session = Session(engine)
        stmt = select(Transaction)
        return session.scalars(stmt)
    except Exception as ex:
        print("Select could not be made due to the following error: \n", ex)
        return 0


"""
It takes an id as an argument, creates a session, creates a statement, and returns the scalar of the
statement

:param id: The id of the transaction to be selected
:return: A single row from the table.
"""
def getTransaction(id):
    try:
        session = Session(engine)
        stmt = select(Transaction).where(Transaction.id == id)
        return session.scalar(stmt)
    except Exception as ex:
        print("Select with id could not be made due to the following error: \n", ex)
        return 0


"""
It takes a name as an argument and returns the transaction with that name

:param name: The name of the transaction
:return: The return value is the first row of the table that matches the name.
"""
def getTransactionName(name):
    try:
        session = Session(engine)
        stmt = select(Transaction).where(Transaction.name == name)
        return session.scalar(stmt)
    except Exception as ex:
        print("Select with name could not be made due to the following error: \n", ex)
        return 0


"""
It deletes a transaction from the database based on the id of the transaction

:param id: The id of the transaction to be deleted
:return: the error message.
"""
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
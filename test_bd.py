from app import db
from app import transaction
from app import api
import unittest

class TestBdd(unittest.TestCase):

    def test_connexion_bd(self):
        engine = db.get_connection()
        self.assertTrue(engine != 0)

    def test_createTable(self):
        engine = db.get_connection()
        self.assertTrue(db.createTable(engine) != 0)
    
    def test_transactionAdd(self):
        form = {}
        form['prix'] = 2
        form['quantite'] = 3
        form['crypto'] = "Bitcoin;4;BTC"
        self.assertTrue(transaction.transactionAdd(form) != 0)

    def test_transactionList(self):
        self.assertTrue(transaction.transactionList() != 0)
   
    def test_getTransaction(self):
        id = 1
        self.assertTrue(transaction.getTransaction(id) != 0)

    def test_getTransactionName(self):
        self.assertTrue(transaction.getTransactionName('Bitcoin') != 0)
    
    def test_getInfoListCrypto(self):
        self.assertTrue(api.getInfoListCrypto() != 0)


if __name__ == '__main__':
    unittest.main()
    
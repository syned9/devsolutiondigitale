from flask import current_app as app
from flask import render_template, request, url_for, redirect
from app import api
from app import transaction

@app.route('/')
def home():
    # transactionList=transaction.transactionList()
    # return transactionList
    return render_template( 'home.html' ,
                           title="Crypto Tracker",
                           description="description",
                           transactionList=transaction.transactionList())

@app.route('/admin/add', methods=('GET', 'POST'))
def adminAdd():
    if request.method == 'POST':
        transaction.transactionAdd(request.form)
        return redirect(url_for('home'))
        
    list=api.getInfoListCrypto()
    listCryptoName={}
    for crypto in list:
        listCryptoName[crypto['name']] = crypto['quote']['EUR']['price']
    return render_template( 'adminAdd.html' ,
                        title="Ajouter une transaction",
                        list=list,
                        listCryptoName=listCryptoName)

@app.route('/admin/del/<int:id>', methods=('GET', 'POST'))
def adminDel(id):
    if request.method == 'POST':
        return transaction.delTransaction(id)

    return render_template( 'adminDel.html' ,
                           title='Supprimer un montant',
                           transaction=transaction.getTransaction(id))

@app.route('/investissement')
def investissement():
    return render_template( 'investissement.html' ,
                           title="Investissements",
                           description="Page pour évaluer ses investissements avec un graphique")
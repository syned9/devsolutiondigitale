from requests import Request, Session
import json
import time
import pprint

"""
It gets the latest information about the top 10 cryptocurrencies from the CoinMarketCap API
:return: A list of dictionaries.
"""
def getInfoListCrypto():
    try :
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=EUR&limit=10"

        payload={}
        headers = {
        'X-CMC_PRO_API_KEY': '57a63591-3979-4c36-b08c-c7b0dd1d93ad'
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(url, data=payload)

        info = json.loads(response.text)['data']

        return info
    except Exception as ex:
        print("Get information from Api could not be made due to the following error: \n", ex)
        return 0
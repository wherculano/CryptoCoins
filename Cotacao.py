import json
import requests
from bs4 import BeautifulSoup

class Cotacao():
    def __init__(self):
        #APIs para consultar os valores
        self.urls = {'hgbrasil':'https://api.hgbrasil.com/finance?format=json',
                     'mercadoBTC':'https://www.mercadobitcoin.net/api/BTC/ticker/',
                    'foxbit':'https://api.blinktrade.com/api/v1/BRL/ticker?crypto_currency=BTC',
                    'poloniex':'https://poloniex.com/public?command=returnTicker',
                    'bitfinex':'https://api.bitfinex.com/v1/pubticker/BTCUSD'}

        for url in self.urls:
            self.req = requests.get(self.urls[url])
            self.dic = json.loads(self.req.text)
            for chave, valor in self.dic.items():
                if url == 'hgbrasil':
                    self.real = self.dic['results']['currencies']['USD']['buy']
                elif url == 'mercadoBTC': 
                    self.val_mercadoBTC = float(valor['last'])
                elif url == 'foxbit':#API antiga da FoxBit. Necessário atualizar para a versão atual.
                    if chave == 'buy':
                        self.val_foxbit = valor
                elif url == 'poloniex':
                    if chave == 'USDT_BTC':
                        self.val_polo = float(valor['last'])
                elif url == 'bitfinex':
                    if chave == 'last_price':
                        self.val_bitfinex = float(valor)
                        
    def mostra_valores(self):
        print('\n{:=^30}'.format('MERCADO BITCOIN'))
        print('  USD {:.2f} | R$ {:.2f}'.format((self.val_mercadoBTC/self.real),self.val_mercadoBTC))
        print('{:=^30}'.format('FOXBIT'))
        print('  USD {:.2f} | R$ {:.2f}'.format((self.val_foxbit/self.real),self.val_foxbit))
        print('{:=^30}'.format('POLONIEX'))
        print('  USD {:.2f} | R$ {:.2f}'.format(self.val_polo,(self.real*self.val_polo)))
        print('{:=^30}'.format('BITFINEX'))
        print('  USD {:.2f} | R$ {:.2f}'.format(self.val_bitfinex,(self.real*self.val_bitfinex)))

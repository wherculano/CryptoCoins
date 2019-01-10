from DataBase import BancoDeDados

import time

class Market(BancoDeDados):
    def __init__(self):
        self.hoje = time.strftime('%d/%m/%Y')
        super().__init__()
        
    #inserir dados na tabela
    def insert(self, moeda, ultimoValor, menorPedido, maiorPedido, maior24hr, menor24hr, volume):
    	self.coin = moeda
    	self.last = ultimoValor
    	self.lowestAsk = menorPedido
    	self.highestBid = maiorPedido
    	self.high24hr = maior24hr
    	self.low24hr = menor24hr
    	self.volume = volume
    	self.cursor.execute("INSERT INTO market (coin, last, lowestAsk, highestBid, high24hr, low24hr, volume, day)\
                            VALUES (?,?,?,?,?,?,?,?)",(self.coin,self.last,self.lowestAsk,self.highestBid,self.high24hr,self.low24hr,self.volume,self.hoje))
    	self.conn.commit()
		
    #visualizar dados da tabela
    def select(self, moeda):
        self.moeda = moeda
        if self.moeda != 'ALL':
            self.cursor.execute("SELECT coin, printf('%.8f', last), printf('%.8f',lowestAsk), printf('%.8f', highestBid), printf('%.8f',high24hr),printf('%.8f',low24hr),\
                                printf('%.8f',volume), day FROM market WHERE coin LIKE '"+self.moeda+"%' ORDER BY day DESC")
            for linha in self.cursor.fetchall():
                print('{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|'.\
                      format('COIN',linha[0],'LAST',linha[1],'LOWEST_ASK',linha[2],'HIGHEST_BID',linha[3],\
                             'HIGH_24Hr',linha[4],'LOW_24Hr',linha[5],'VOLUME',linha[6],'DATA',linha[7]))
                print('='*34)
        else:
            self.cursor.execute("SELECT coin, printf('%.8f', last), printf('%.8f',lowestAsk), printf('%.8f', highestBid), printf('%.8f',high24hr),printf('%.8f',low24hr),\
                                printf('%.8f',volume), day FROM market ORDER BY day DESC")
            for linha in self.cursor.fetchall():
                print('{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|\n{:<12}|{:^20}|'.\
                      format('COIN',linha[0],'LAST',linha[1],'LOWEST_ASK',linha[2],'HIGHEST_BID',linha[3],\
                             'HIGH_24Hr',linha[4],'LOW_24Hr',linha[5],'VOLUME',linha[6],'DATA',linha[7]))
                print('='*34)

import sqlite3
import io

class BancoDeDados:
    def __init__(self):
        ##conectando ao banco
        self.conn = sqlite3.connect('CryptoCoins.db')
        #cursor que executará os comandos sql
        self.cursor = self.conn.cursor()
                
    def criar(self):
        #criando a tabela Historico
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            day TEXT NOT NULL,
            coin TEXT NOT NULL,
            amount REAL NOT NULL);""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS market(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            coin TEXT NOT NULL,
            last REAL NOT NULL,
            lowestAsk REAL NOT NULL,
            highestBid REAL NOT NULL,
            high24hr REAL NOT NULL,
            low24hr REAL NOT NULL,
            volume REAL NOT NULL,
            day TEXT NOT NULL);""")        
        print('Tabelas  com sucesso!')

    #inserir dados na tabela
    def insert(self, *args):#moeda, valor
        pass
		
    #visualizar dados da tabela
    def select(self,*args):
        pass

    def __backup(self):
        with io.open('CryptoCoins_Backup.sql','w') as bkp:
            #(iterdump)exporta a estrutura do banco e os dados para um arquivo externo
            for linha in self.conn.iterdump():
                bkp.write('%s\n' % linha)
        print('Backup realizado com sucesso!')
        print('Salvo no diretório atual como CryptoCoins_Backup.sql')

    def __restoreBackup(self):
        self.rest = io.open('CryptoCoins_Backup.sql','r')
        self.sql = self.rest.read()
        self.cursor.executescript(self.sql)
        print('Banco de Dados recuperado com sucesso!')
        

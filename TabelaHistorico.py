from DataBase import BancoDeDados
import time

class Historico(BancoDeDados):
    def __init__(self):
        self.hoje = time.strftime('%d/%m/%Y')
        super().__init__()
        
    #inserir dados na tabela
    def insert(self, moeda, valor):
    	self.coin = moeda
    	self.value = valor
    	self.cursor.execute("INSERT INTO historico (day,coin,amount) VALUES (?,?,?)",(self.hoje,self.coin,self.value))
    	self.conn.commit()
		
    #visualizar dados da tabela
    def select(self,moeda='all'):
        self.op = moeda
        if self.op == 'all':
            self.cursor.execute("SELECT day, coin, printf('%.8f', amount) FROM historico ORDER BY day DESC")
            for linha in self.cursor.fetchall():
                data = linha[0]
                print(*linha)
                if linha[0] !=  data:
                    print('-='*30)
        else:
            self.cursor.execute("SELECT day, coin, printf('%.8f', amount) FROM historico WHERE coin LIKE ? ORDER BY day DESC",(self.op,))
            for linha in self.cursor.fetchall():
                print(*linha)
                print('-='*30)


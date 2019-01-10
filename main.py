import os
import time
from Balance import Balance
from Cotacao import Cotacao
from DataBase import BancoDeDados
from TabelaHistorico import Historico
from TabelaMarket import Market
from poloniex import poloniex


#API Key e Secret Key (Poloniex)
api = '<colar API>'
secret = '<colar Secret>'

#Instancia da Classe Poloniex        
polo = poloniex.Poloniex(api,secret)

#Variável que recebe a função que retorna os valores disponíveis
montanteTotal = polo.returnCompleteBalances('all')
valoresDiarios = polo.returnTicker()

#Construtor do Banco de Dados
bd = BancoDeDados()

#Construtor da Tabela Historico
historico = Historico()

#Construtor da Tabela Market
market = Market()

#Construtor da Classe que pega a cotação do BTC
cotacao = Cotacao()

#Função para limpar a tela ao rodar o programa via terminal
def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')       
                             
while True:
    while True:
        try:
            limpar()
            #Menu inicial
            print('{:=^30}'.format('MENU'))
            op = int(input('''1- Banco de Dados
2- Cotação do BTC
3- Historico Poloniex
4- Markets
5- Balance
6- Sair
Opção: '''))
            
            break
        except ValueError:
            print('\nDigite apenas uma das opções acima!\n')
            input('Press <ENTER>\n')
            
    #Cria o Banco de Dados no Diretório Atual
    if op == 1:
        while True:
            try:
                limpar()
                print('{:=^30}'.format('MENU'))
                opc = int(input('''1- Criar Banco de Dados\n2- Fazer Backup\n3- Restaurar Backup\n4- Voltar\nOpção: '''))
            except ValueError:
                print('\nDigite apenas uma das opções acima!\n')
                input('Press <ENTER>\n')
            if opc == 1:
                bd.criar()
                input('\nPress <ENTER>\n')
            elif opc == 2:
                bd._BancoDeDados__backup()
                input('\nPress <ENTER>\n')
            elif opc == 3:
                bd._BancoDeDados__restoreBackup()
                input('\nPress <ENTER>\n')
            elif opc == 4:
                break
    #Mostra a contação do Bitcoin
    elif op == 2:
        limpar()
        cotacao.mostra_valores()
        input('\nPress <ENTER>\n')
    #Menu para visualizar ou atualizar os valores
    elif op == 3:
        while True:
            try:
                limpar()
                print('{:=^30}'.format('MENU'))
                opBD = int(input('''1- Atualizar Valores\n2- Visualizar Historico\n3- Voltar\nOpção: '''))
            except ValueError:
                print('\nDigite apenas uma das opções acima!\n')
                input('Press <ENTER>\n')
            #Carrega os valores e salva no Banco de Dados
            if opBD == 1:
                limpar()
                print('Aguarde...')
                for k,v in montanteTotal.items():
                    if (montanteTotal[k]['available'] > 0) or (montanteTotal[k]['onOrders'] > 0) or (montanteTotal[k]['btcValue'] > 0):
                        total = montanteTotal[k]['onOrders']+montanteTotal[k]['available']
                        historico.insert(k,total)
                input('Banco de Dados atualizado\nPress <ENTER>\n')
            #Busca as informações no Banco de Dados
            elif opBD == 2:
                while True:
                    limpar()
                    print('Suas Moedas disponiveis para ver o Historico sao:\n')
                    for k,v in montanteTotal.items():
                        if (montanteTotal[k]['available'] > 0) or (montanteTotal[k]['onOrders'] > 0) or (montanteTotal[k]['btcValue'] > 0):
                            print('| {} '.format(k),end='')
                    choice = input('\n\nDigite a sigla da moeda ou "all" para listar todas: ').upper()
                    print('\n')
                    if choice == 'ALL':
                        historico.select()
                    else:
                        historico.select(choice)
                    sair = input('\nDeseja selecionar outra moeda? [S/N]: ')
                    if sair in 'Nn':
                        break                    
                input('\nPress <ENTER>\n')
            #Volta para o Menu anterior
            elif opBD == 3:
            	break
    elif op == 4:
        limpar()
        while True:
            try:
                limpar()
                print('{:=^30}'.format('MENU'))
                opBD = int(input('''1- Atualizar Valores\n2- Visualizar Historico\n3- Voltar\nOpção: '''))
            except ValueError:
                print('\nDigite apenas uma das opções acima!\n')
                input('Press <ENTER>\n')
            #Carrega os valores e salva no Banco de Dados
            if opBD == 1:
                limpar()
                for coin, info in sorted(valoresDiarios.items()):
                    market.insert(coin, info['last'], info['lowestAsk'],info['highestBid'],info['high24hr'],info['low24hr'],info['baseVolume'])
                print('Banco de Dados Atualizado!')
                time.sleep(1)
            #Busca as informações no Banco de Dados
            elif opBD == 2:
                while True:
                    while True:
                        try:
                            op = input('\nDigite a sigla da moeda [BTC, ETH, XMR, USDT] ou ALL para ver os valores!\nSigla: ').upper()
                            break
                        except:
                            print('Digite uma opção válida!')
                    limpar()
                    market.select(op)
                    sair = input('\nDeseja selecionar outra moeda? [S/N]: ')
                    if sair in 'Nn':
                        break                    
                input('\nPress <ENTER>\n')
            #Volta para o Menu anterior
            elif opBD == 3:
            	break
        input('\nPress <ENTER>\n')
    elif op == 5:
        print('\nAguarde ...')
        input('\nPress <ENTER>\n')
    elif op == 6:
        input('\nPress <ENTER>\n')
        break

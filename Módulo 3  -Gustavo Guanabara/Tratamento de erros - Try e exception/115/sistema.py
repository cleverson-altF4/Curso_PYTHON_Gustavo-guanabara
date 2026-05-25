from biblioteca.interface import *


from time import sleep

cabecalho("Sistema de cadastro")
while True:
    resposta = menu(['Ver pessoas cadastradas', 'cadastrar pessoas', 'Sair do sistema'])
    
    if resposta == 1:
        cabecalho("Opção 1")
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        cabecalho("Opção 3")
        break
    else:
        print("Erro! Digite uma opção válida")
        sleep(1.5)
#jogo pedra papel e tesoura
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''  \n-Opções-\n
[0] - Pedra  
[1] - Papel
[2] - Tesoura\n''')

jogador = int(input("Selecione um número: ")) 
amarelo = '\033[33m'
print(amarelo + 'Jo')
sleep(1)
print("ken")
sleep(1)
print("po!!!")
sleep(1)
print(f"O computador escolheu: {itens[computador]}")
print(f"Eu escolhi {itens[jogador]}")

if computador == 0:  # computador jogou pedra e eu joguei pedra (empate)
    if jogador == 0: 
        print("empate")
    elif jogador == 1: #computador jogou pedra e eu joguei papel (eu ganho)
        print("Eu ganhei")
    elif jogador == 2: #computador jogou pedra e eu joguei tesoura (Computador ganha)
        print("Computador venceu")
    else:
        print("jogada inválida")
elif computador == 1: #computador jogou papel
    if jogador == 0: #pedra
        print("Computador venceu")
    elif jogador == 1: #joguei papel
        print("Empate")
    elif jogador == 2: # tesoura
        print("Eu venci")
    else:
        print("Jogada inválida")
elif computador == 2: #tesoura
    if jogador == 0: #pedra
        print("Eu venci")
    elif jogador == 1:
        print("Computador venceu")
    elif jogador == 2:
        print("empate")
    else:
        print("Jogada inválida")

    

#melhore um jogo onde o computador vai pensar em um número entre um número de 0 á 10
#so que agora o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites fora necessários para vencer

from random import randint
import emoji

computador = randint(0,10)
acertou = False #Bool
tentativas = 0

while not acertou:
    jogador = int(input("Qual é o seu palpite: "))
    tentativas += 1
    
    if jogador == computador:
        acertou = True # Bool
    else:
        if jogador < computador:
            print(emoji.emojize(":pinching_hand: Mais um pouquinho\n"))
        elif jogador > computador:
             print("Menos ➖.\n")
        
        
print("Acertou 🎉\n")
print("Tentativas : {}x\n".format(tentativas))
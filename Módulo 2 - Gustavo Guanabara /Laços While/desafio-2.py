#melhore um jogo onde o computador vai pensar em um número entre um número de 0 á 10
#so que agora o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites fora necessários para vencer

from random import randint

tentativas = 0
palpite = 0
numero_secreto = randint(0,11)

while palpite != numero_secreto:
    palpite = int(input("Digite o número: "))
    tentativas += 1
    
    if palpite < numero_secreto:
        print("Está próximo de ganhar\n")
    elif palpite > numero_secreto:
        print("Passou quase perto\n")
    
print("Você venceu")
print(f"Você teve {tentativas} tentativas até acertar o número")
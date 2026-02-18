#Faça um programa que ajude um jogador da Mega Sena a criar palpite.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
jogos = []


quantidade_jogos = int(input("Deseja quantos jogos? "))
total = 1

while total <= quantidade_jogos:
    contador = 0
    
    while True:
        numero = randint(1, 60)
        
        if numero not in lista:
            lista.append(numero)
            contador += 1
            
        if contador >= 6:
            break
        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, list in enumerate(jogos):
    print(f"JOGOS {i + 1} - {list}")
    sleep(1)


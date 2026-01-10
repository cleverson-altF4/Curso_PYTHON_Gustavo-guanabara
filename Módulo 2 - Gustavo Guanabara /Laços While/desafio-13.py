#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder.mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint

vitorias = 0

while True:
    numero = int(input("Digite um número: "))
    par_impar = str(input("par ou ìmpar? ")).strip().upper()[0]
    if par_impar in 'Pi':
        
    computador = randint(1,11)
    soma = numero + computador
    
    if soma % 2 == 0:
        res = 'par'
    else:
        res = 'ímpar'
        
    if numero == computador:
        print("Acertei")
        print("tente novamente\n")
        vitorias + 1
    else:
        print("Perdi")
        break
    
    print("*"*10, "Jogo de advinhação", "*"*10)
print("Total de vitórias = {}".format(vitorias))
    

        
    
    
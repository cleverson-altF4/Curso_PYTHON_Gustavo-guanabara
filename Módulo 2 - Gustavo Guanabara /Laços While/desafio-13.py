#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder.mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
vitorias = 0

while True:
    numero = int(input("Digite um número: "))
    par_impar = input("par ou ìmpar? ").strip().upper()[0]
    
    if par_impar not in ('P', 'I'):
        print("Apenas é permitido par ou ìmpar")
        continue
    
    computador = randint(0, 11)
    soma = numero + computador
    
    print(f"joguei {numero}")
    print(f"O computador jogou {computador}")
    print(f"A soma = {soma}")
    
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
        
    if resultado == par_impar:
        print("Eu venci")
        vitorias += 1
    else:
        print("Eu perdi")
        break
        
    
print(f"Vitórias consecutivas: {vitorias}")
       
        
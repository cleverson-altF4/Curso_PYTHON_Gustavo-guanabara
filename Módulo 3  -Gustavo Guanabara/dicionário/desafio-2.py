#Crie um programa que onde 4 jogadores joguem um dado e tenham resultados.
#Guarde em um dicionário
#No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número do dado

from random import randint

jogadores = {}

for i in range(1, 5):
    dado = randint(1, 6)
    jogadores[f"Jogador {i}"] = dado
    
print("-"*30)
print("    Resultados   ")
print("-"*30)

for jogador, res in jogadores.items():
    print(f"{jogador} = {res}")
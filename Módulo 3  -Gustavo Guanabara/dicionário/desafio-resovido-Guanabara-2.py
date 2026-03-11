#Crie um programa que onde 4 jogadores joguem um dado e tenham resultados.
#Guarde em um dicionário
#No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número do dado

from random import randint
from time import sleep
from operator import itemgetter
import emoji


jogador = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}


ranking = {}

for k, v in jogador.items():
    print(f"{k} tirou {v}")
    sleep(1)
    
print("-"*30)
print("     Ranking     ")
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

for i, valor in enumerate(ranking):
    print(f"{i+1}° colocado {valor[0]}: {valor[1]}")
    sleep(1)
    
print("-"*30)
print("  Lista de jogadores   ")

for i in ranking:
    if i[1] == 1:
        print(f"Jogador {i[0]} tirou 1")
    elif i[1] == 2:
        print(f"Jogador {i[0]} tirou 2")
    elif i[1] == 3:
        print(f"Jogador {i[0]} tirou 3")
    elif i[1] == 4:
        print(f"Jogador {i[0]} tirou 4")
    elif i[1] == 5:
        print(f"JOgador {i[0]} tirou 5")
    elif i[1] == 6:
        print(emoji.emojize(f"O vencedor foi o {i[0]} :trophy:", language='alias'))
    else:
        print("Não teve vencedor")
from random import randint
from operator import itemgetter
from time import sleep
import emoji

jogo = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}

rankink = {}

for k, c in jogo.items():
    print(f"{k}: {c}")
    sleep(1)
    
rankink = sorted(jogo.items(), key=itemgetter(1), reverse=True)

    
print(f"   resultado    ")
for i in rankink:
    if i[1] == 1:
        print(f"{i[0]} tirou {i[1]}")
    elif i[1] == 2:
        print(f"{i[0]} tirou {i[1]}")
    elif i[1] == 3:
        print(f"{i[0]} tirou {i[1]}")
    elif i[1] == 4:
        print(f"{i[0]} tirou {i[1]}")
    elif i[1] == 5:
        print(f"{i[0]} tirou {i[1]}")
    elif i[1] == 6:
        print(emoji.emojize(f"O vencedor foi o {i[0]} :trophy:", language='alias'))
    else:
        print("Ninguém jogou o dado")
        
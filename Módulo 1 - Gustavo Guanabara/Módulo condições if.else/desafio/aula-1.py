import random #biblioteca jogo
from time import sleep # do tempo importando contagem
jogo = int(input("Advinha o número de 1 à 5 ")) 
sorteio = random.randint(1, 5)  
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
if jogo == sorteio:
    print("Acertou, parabéns")
else:
    print("Tente novamente.")
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for i in range(1,8):
    nascido = int(input(f"{i} - Em que ano você nasceu: "))
    idade = atual - nascido
    if idade >= 18:
        print(f"Fulano nasceu em {nascido}")
        print(f"Fulano tem {idade} anos")
        totalmaior += 1
    else:
        print(f"Fulano nasceu em {nascido}")
        print(f"Fulano tem {idade} anos")
        totalmenor += 1


print("Total maior de idade {}".format(totalmaior))
print("Total menor de idade {}".format(totalmenor))

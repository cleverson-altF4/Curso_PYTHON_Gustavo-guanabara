from datetime import date
atual = date.today().year
nascimento = int(input("Qual é a sua data de nascimento: "))
idade = atual - nascimento
print(f"A sua data de nascimento é de {nascimento}, sua idade é {idade} e o ano atual que você está é em {atual}")
if idade == 18:
    print("Você tem idade suficiente para carreira militar")
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f"Você não tem idade idade suficiente ")
    print(f"Ainda falta {saldo} anos para ingressar")
    print(f"Você irá ingressar em {ano}")
else:
    saldo = idade - 18
    ano = atual + saldo
    print("Você passou da idade e não pode mais se alistar.")
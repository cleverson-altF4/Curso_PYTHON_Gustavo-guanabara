from datetime import date
atual = date.today().year
ano = int(input("Qual é a sua data de nascimento: "))
idade = atual - ano
print(f"Você é do ano de {ano}")
print(f"Você está em {atual}")
print(f"Você tem {idade} anos")

if idade < 10:
    categoria = 'Mirin'
elif idade < 15:
    categoria = 'Juvenil'
elif idade < 18:
    categoria = 'Amador'
elif idade < 25:
    categoria = 'profissional'
else:
    categoria = 'Master'

print(f"A categoria = {categoria}")
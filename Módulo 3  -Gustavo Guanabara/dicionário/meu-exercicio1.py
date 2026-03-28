#Exercício: Cadastro Simples com Dicionário
# Objetivo:
#Criar um programa que:
#Cadastre 1 pessoa
#Guarde:
#nome
#idade
#cidade
#Mostre os dados na tela

from datetime import datetime

print("-"*35)
print("    Cadastro      ")


cadastro = {}
cadastro['nome'] = str(input("Nome da pessoa: ")).strip()
cadastro['idade'] = int(input("Idade: "))
cadastro['cidade'] = str(input("Cidade: ")).strip()

print("-"*35)
print("    Dados do cadastro     ")

for keys, valores in cadastro.items():
    if keys == 'nome' or keys == 'idade':
        print(f"{keys}: {valores}")
    
data_atual = datetime.now().year

for keys, valores in cadastro.items():
    
    if keys == 'idade':
        data_nascimento = (data_atual - valores) - 1
        print(f"Data de nascimento: {data_nascimento}")


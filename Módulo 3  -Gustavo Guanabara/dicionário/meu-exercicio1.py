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
print("-"*30)
print("      Cadastro de alunos     ")
print("-"*30)
cadastro = {}

cadastro['nome'] = str(input("Digite seu nome: ")).strip()
cadastro['idade'] = int(input("Digite a sua idade: "))
cadastro['cidade'] = str(input("Qual é a sua cidade: "))

print("-"*30)
print("Dados do cadastro")


for chaves, valores in cadastro.items():
    if chaves == 'nome' or chaves == 'idade':
        print(f"{chaves} : {valores}")

ano_atual = datetime.now().year

for chaves, valores in cadastro.items():
    
    if chaves == 'idade':
        data_nascimento = ano_atual - valores
        print(f"Data de nascimento: {data_nascimento}")
        




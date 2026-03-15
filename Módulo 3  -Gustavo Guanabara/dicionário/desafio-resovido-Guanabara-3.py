#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os com idade em dicionário se por acaso a cttps for diferente de zero o dicionário receberá também o ano de contratação e o salário. Calcule o acrescente além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime

dados = {}
dados['nome'] = str(input("Digite o seu nome: ")).strip()
data_nascimento = int(input("Ano em que nasceu: "))
dados['idade'] = datetime.now().year - data_nascimento
dados['cttps'] = int(input("Carteira de trabalho: "))

if dados['cttps'] != 0:
    dados['contratacao'] = int(input("Ano que foi contratado: "))
    dados['salario'] = float(input("Valor do salário R$: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
    
for k, v in dados.items():
    print(f"{k}: {v}")
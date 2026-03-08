#Faça um programa que leia nome e média de um aluno guardando também a sintuação em um dicionário.No final mostre o conteúdo da estrutura na tela

aluno = {}

aluno['Nome'] = str(input("Nome: ")).strip()
aluno['media'] = float(input(f"Média de {aluno['Nome']}: "))


if aluno['media'] >= 7:
    sintuacao = 'Aprovado'
else:
    sintuacao = 'Reprovado'
    
    
for posicao, valor in aluno.items():
    print(f"{posicao}: {valor}")
   
print(f"sintuação: {sintuacao}")
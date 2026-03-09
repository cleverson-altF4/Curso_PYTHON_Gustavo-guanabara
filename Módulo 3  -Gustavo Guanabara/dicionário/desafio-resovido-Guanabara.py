#Faça um programa que leia nome e média de um aluno guardando também a sintuação em um dicionário.No final mostre o conteúdo da estrutura na tela


aluno = {}
aluno['Nome'] = str(input("Nome: ")).strip()
aluno['media'] = float(input(f"Média do {aluno['Nome']}: "))
if aluno['media'] >= 7:
    aluno['sintuacao'] = 'Aprovado'
elif aluno['media'] < 7:
    aluno['sintuacao'] = 'Recuperação'
else:
    aluno['sintuacao'] = 'Reprovado'
    
print("-"*30)
print("   Resultado    ")

print(f"Aluno: {aluno['Nome']}")
print(f"Média: {aluno['media']} pontos")
print(f"Sintuação: {aluno['sintuacao']}")
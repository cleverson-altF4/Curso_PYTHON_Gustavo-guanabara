#Dicionário dentro de lista (muito usado)

#Exemplo: cadastro de alunos
alunos = []
for i in range(2):
    aluno = {}
    aluno['Aluno'] = str(input("Aluno: "))
    aluno['Nota'] = float(input("Notas:"))
    alunos.append(aluno)
    
print(alunos)

#Isso cria uma lista de dicionários.
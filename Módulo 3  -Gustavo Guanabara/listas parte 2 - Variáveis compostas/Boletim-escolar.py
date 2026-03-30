boletim = []

print("   Boletim Escolar   ")

while True:
    nome = input("Digite o nome do aluno: ").strip()
    primeiro_bimestre = float(input("Primeiro bimestre: "))
    segundo_bimestre = float(input("Segundo bimestre: "))
    terceiro_bimestre = float(input("Terceiro bimestre: "))
    quarto_bimestre = float(input("Quarto bimestre: "))
    
    media = round((primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre) / 4, 2)
    
    aluno = {
        'Nome': nome,
        'Notas': [primeiro_bimestre, segundo_bimestre, terceiro_bimestre, quarto_bimestre],
        'Media': media,
        
    }    
    
    boletim.append(aluno)
    
    
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim ou Nao]: ")).strip().upper()
        if continuar == '':
            print("\nEspaço em branco. digite novamente\n")
            
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print("    Resultado   ")

for aluno in boletim:
    print(f"Aluno: {aluno['Nome']}")
    print(f"Média: {aluno['Media']:.2f}")
    
    if aluno['Media'] >= 12:
        print("Situação: Aprovado")
    else:
        faltou = 12 - aluno['Media']
        print(f"Situação:(faltou: {faltou:.2f} pontos)")
    
    print("_" * 30) 
    
    
print("    Lista de alunos Aprovados/Reprovados   ")
for i, total in enumerate(boletim):
    if total['Media'] >= 12:
       print(f"Aprovados: {total['Nome']}")
    else:
        print(f"Reprovados: {total['Nome']}")

    
        


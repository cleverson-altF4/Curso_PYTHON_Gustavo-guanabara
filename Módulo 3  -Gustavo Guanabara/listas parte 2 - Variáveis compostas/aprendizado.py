print('-'*40)
print('-'*10,"Cadastro de alunos",'-'*10)
print('-'*40)

print()

dados = []
lista_com_dados = []


while True:
    print('''
      1 - Cadastro de alunos
      2 - Listar alunos
      3 - Mostrar aprovados e reprovados
      4 - Mostrar maior nota
      5 - Buscar por aluno desejado
      6 - Sair''')
    
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        
        dados.append(str(input("Digite o seu nome: ")).strip())
        dados.append(float(input("Digite a sua nota: ")))
        lista_com_dados.append(dados[:])
        dados.clear()
    elif opcao == 2:
        
        if lista_com_dados == []:
            print("A lista está vazia")
        else:
            print("\nA lista de alunos:")
            
            for i, aluno in enumerate(lista_com_dados):
                print(f"Aluno {i + 1} - Nome = {aluno[0]}  Nota = {aluno[1]}")
            
        
        
        
    
   
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
        print("\n~ ---- Cadastro -----~")
        dados.append(str(input("Digite o seu nome: ")).strip())
        dados.append(float(input("Digite a sua nota: ")))
        lista_com_dados.append(dados[:])
        dados.clear()
    elif opcao == 2:
        print("\n~ ---- Lista dos alunos -----~")
        if lista_com_dados == []:
            print("A lista está vazia")
        else:
            
            for i, aluno in enumerate(lista_com_dados):
                print(f"Aluno {i + 1} - Nome = {aluno[0]}  Nota = {aluno[1]}")
    elif opcao == 3:
        print("\n~ ---- Sintuação do aluno -----~")
        for aluno in lista_com_dados:
            if aluno == []:
                print("Não há aluno matriculado")
            else:
                if aluno[1] >= 7:
                    print(f"Aluno(a) {aluno[0]} = Aprovado")
                else:
                    print(f"Aluno(a) {aluno[0]} = Reprovado")
    elif opcao == 4:
        

        print("\n~ ---- Maior e Menor Nota -----~")

        if lista_com_dados == []:
            print("Não há alunos cadastrados.")
        else:
            #variáveis 
            maior = lista_com_dados[0][1]
            menor = lista_com_dados[0][1]
            
            lista_maior = [lista_com_dados[0][0]]
            lista_menor = [lista_com_dados[0][0]]
            
            for aluno in lista_com_dados[1:]:
                if aluno[1] > maior:
                    maior = aluno[1]
                    lista_maior = [aluno[0]]
                    
                elif aluno[1] == maior:
                    lista_maior.append(aluno[0])
                    
                    
                if aluno[1] < menor:
                    menor = aluno[1]
                    lista_menor = [aluno[0]]
                
                    
                elif aluno[1] == menor:
                    lista_menor.append(aluno[0])
                    
                    
            print("-"*40)
            print(f"Maior nota: {maior} - Alunos(a): {', '.join(lista_maior)}")
            print(f"Maior nota: {menor} - Aluno(a): {', '.join(lista_menor)}")
    elif opcao == 5:
        if lista_com_dados == []:
            print("Não há alunos para a busca")
            break
        else:
            busca_aluno = str(input("Deseja pesquisar qual aluno: "))
            encontrado = False
            
            for aluno in lista_com_dados:
                if busca_aluno == aluno:
                    encontrado = True
                    

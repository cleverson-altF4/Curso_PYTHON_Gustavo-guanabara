from time import sleep
print("-"*40)
print("     - Sistema de cadastro escolar -     \n")
print("-"*40)

dados = []
lista_com_dados = []

while True:
    
    print('''
        1 - Cadastrar aluno
        2 - lista de alunos cadastrados
        3 - Lista de alunos aprovados/reprovados
        4 - Mostrar a maior nota
        5 - Buscar por aluno
        6 - Sair do programa''')
    
    opcao = int(input("\nSelecione uma opção: "))
    
    
    
    if opcao == 1:
        print(" ----------- Cadastrar aluno ----------- ")
        dados.append(str(input("Nome do aluno: ")).strip())
        dados.append(float(input("Qual foi a nota do aluno: ")))
        lista_com_dados.append(dados[:])
        dados.clear()
    elif opcao == 2:
        print("-"*40)
        print("     - Lista completa -")
        print()
        if lista_com_dados == []:
            print("Lista vazia")
        else:
            for i, aluno in enumerate(lista_com_dados):
             print(f"{i + 1} - {aluno[0]}")
    elif opcao == 3:
        print(" ----------- aprovados/reprovados ----------- ")
        if lista_com_dados == []:
            print("Não há aluno matriculado")
        else:
            for i, aluno in enumerate(lista_com_dados):
                if aluno[1] >= 7:
                    print(f"{i + 1} - {aluno[0]} - \033[32mAprovado\033[m")
                else:
                    print(f"{i + 1} - {aluno[0]} - \033[31mReprovado\033[m")
    elif opcao == 4:
        maior = lista_com_dados[0][1]
        menor = lista_com_dados[0][1]
        
        nome_maior = [lista_com_dados[0][0]]
        nome_menor = [lista_com_dados[0][0]]
            
        for aluno in lista_com_dados[1:]:
            if aluno[1] > maior:
                maior = aluno[1]
                nome_maior = [aluno[0]]
                
            elif aluno[1] == maior:
                nome_maior.append(aluno[0])
                
            if aluno[1] < menor:
                menor = aluno[1]
                nome_menor = [aluno[0]]
                
            elif aluno[1] == menor:
                nome_menor.append(aluno[0])
        print(f"Maior nota: \033[32m{maior}\033[m")
        print(f"Alunos com a maior nota: {', '.join(nome_maior)}")
        print(f"Menor nota: \033[31m{menor}\033[m")
        print(f"Alunos com a menor nota: {', '.join(nome_menor)}")
    elif opcao == 5:
        buscar_aluno = str(input("Procurar aluno: ")).strip()
        encontrado = True
        
        if lista_com_dados == []:
            print("Não há aluno matriculado")
        else:
            for aluno in lista_com_dados:
                if aluno[0] == buscar_aluno:
                    encontrado = True
                    print(f"Aluno {aluno[0]} encontrado")
                else:
                    encontrado = False
                    print("Não tem registro do aluno procurado")
    else:
        
        print("Saindo do programa")
        sleep(2)
        break
                
                
        
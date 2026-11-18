from encodings import euc_kr
from time import sleep

from rich import syntax

dados = []
lista_com_dados = []
def cabecalho():
    print("*"*40)
    print("---- Sistema de cadastro escolar ----- ")
    print("*"*40)
def Menu():
    while True:
        print("1 - Cadastrar aluno")
        print("2 - Lista de alunos cadastrados")
        print("3 - Lista de alunos (aprovados/reprovados)")
        print("4 - Mostrar a maior nota")
        print("5 - Buscar aluno")
        print("6 - Sair do programa")

        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            print("="*7, "Cadastrar Aluno", "="*7 )
            dados.append(str(input("Nome do aluno: ")))
            dados.append(float(input(f"Nota do aluno: ")))
            lista_com_dados.append(dados[:]) #Se não adicionar [:] tem duplicatas
            dados.clear()
        elif opcao == 2:
            print("="*7, "Lista completa", "="*7 )
            if lista_com_dados == []:
                print("Lista está vazia")
            else:
                for posicao, aluno in enumerate(lista_com_dados):
                    print(f"{posicao+1}: {aluno[0]}")
        elif opcao == 3:
            print("=" * 7, "Lista alunos aprovados/reprovados", "=" * 7)

            if lista_com_dados == []:
                print("Não há alunos registrados")
            else:
                for posicao, aluno in enumerate(lista_com_dados):
                    if aluno[1] >= 7:
                        print(f"Aluno {aluno[0]} - Aprovado")
                    else:
                        print(f"Aluno {aluno[0]} - Reprovado")
        elif opcao == 4:
            print("=" * 7, "Aluno com a maior nota", "=" * 7)

            if not lista_com_dados:
                print("Não há aluno registrado")
            else:
                maiorNota = lista_com_dados[0][1]
                menorNota = lista_com_dados[0][1]

                nomeMaior = [lista_com_dados[0][0]]
                nomeMenor = [lista_com_dados[0][0]]

                for aluno in lista_com_dados[1:]:
                    if aluno[1] > maiorNota:
                        maiorNota = aluno[1]
                        nomeMaior = [aluno[0]]
                    elif aluno[1] == maiorNota:
                        nomeMaior.append(aluno[0])

                    if aluno[1] < menorNota:
                        menorNota = aluno[1]
                        nomeMenor = aluno[0]
                    elif aluno[1] == menorNota:
                        nomeMenor.append(aluno[0])

                print(f"Aluno: {''.join(nomeMaior)} | Maior nota: {maiorNota}")
                print(f"Aluno: {''.join(nomeMenor)} | Menor nota: {menorNota}")
        elif opcao == 5:
            if not lista_com_dados:
                return f"Não há alunos na busca"
            else:
                buscarNome = str(input("Buscar por aluno: ")).strip()
                encontrado = False
                for busca in lista_com_dados:
                    if busca[0].lower() == buscarNome.lower():
                        print(f'Aluno {busca[0]} encontrado | Nota: {busca[1]}')
                        encontrado = True
                    else:
                        if not encontrado:
                            print("Não foi encontrado ")
        else:
          print("Saindo do programa")
          sleep(3)
          break
#**********************
cabecalho()
Menu()

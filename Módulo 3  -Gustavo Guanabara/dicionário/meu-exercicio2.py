from datetime import datetime
from time import sleep
print("-"*40)
print("       - Sistem de cadastro -     ")


print("-"*40)

lista = [] #lista

while True:
   
    print('''
      1 - Cadastro de alunos
      2 - Listas dos alunos
      3 - Alunos maior ou menor idade
      4 - sair do programa''')
    print("-"*40)
  
    opcao = int(input("Digite a sua opção: "))
    print("\n")
    
    if opcao == 1:
        aluno = {} # dicionário
        aluno["nome"] = str(input("Digite o seu nome: ")).strip()
        aluno["idade"] = int(input("Digite a sua idade: "))
        aluno["cidade"] = str(input("Qual a sua cidade: ")).strip()
        lista.append(aluno)
        print("Aluno cadastrado com sucesso!")
    elif opcao == 2:
        if len(lista) == 0:
            print("Não há aluno cadastrado")
        else:
            ano_atual = datetime.now().year
            for pessoa in lista:
                print(f'Nome: {pessoa["nome"]}')
                print(f'Idade: {pessoa["idade"]}')
                print(f'Cidade: {pessoa["cidade"]}')
                data_nascimento = ano_atual - pessoa["idade"]
                print(f"Data de nascimento:  {data_nascimento}")
                print("-"*40)
            print()
    elif opcao == 3:
        maior = lista[0]["idade"]
        menor = lista[0]["idade"]
        
        nome_maior = lista[0]["nome"]
        nome_menor = lista[0]["nome"]
        
        if len(lista) == 0:
            print("Não há aluno cadastrado!")
        else:
            for pessoa in lista:
                if pessoa["idade"] > maior:
                    maior = pessoa["idade"]
                    nome_maior = pessoa["nome"]
                    
                if pessoa["idade"] < menor:
                     menor = pessoa["idade"]
                     nome_menor = pessoa["nome"]
                     
            print(f'O aluno com a maior idade: {nome_maior}: {maior} anos')
            print(f'O aluno com a menor idade: {nome_menor} {menor} anos')
            
    elif opcao == 4:
        if opcao == 4:
            print("Finalizando programa")
            sleep(1.3)
            break
        else:
            print("Opção invalida!")
                    
            
                
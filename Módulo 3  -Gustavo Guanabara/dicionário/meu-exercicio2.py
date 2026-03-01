from datetime import datetime

pessoas = [] # Lista
print("\n", "-"*40)
    
print("       - Sistema de cadastro -     ")

while True:
    
    print('''
          1 - cadastrar aluno
          2 - Listar pessoas 
          3 - Idade é maior ou menor
          4 - sair''')
    
    opcao = int(input("Deseja qual opção? "))
    
    print("-"*40)
    
    if opcao == 1:
        pessoa = {} # Dicionário
        pessoa["nome"] = str(input("Digite o seu nome: ")).strip()
        pessoa["idade"] = int(input("Sua idade: "))
        pessoa["cidade"] = str(input("Sua cidade: ")).strip()
        pessoas.append(pessoa)
        print("Cadastro realizado com sucesso!")
    if opcao == 2:
        if len(pessoas) == 0:
            print("Não há aluno cadastrado")
        else:
            ano_atual = datetime.now().year

            for p in pessoas:
                print("-"*30)
                print("Nome:", p["nome"])
                print("Idade:", p["idade"])
                print("Cidade:", p["cidade"])

                ano_nascimento = ano_atual - p["idade"]
                print("Ano de nascimento:", ano_nascimento)
                
    elif opcao == 3:
        if len(pessoas) == 0:
            print("Não há aluno cadastrado")
        else:
            maior = 0
            
            for p in pessoas:
                if p["idade"] > maior:
                    maior = p["idade"]
                    
            print(f"A pessoa com maior maior cadastrado:  {maior} anos")
    elif opcao == 4:
        if opcao == 4:
            break
        else:
            print("opção inválida")
        
        
cadastros = []

def Menu():
    print('''
          [1] - Cadastrar pessoa
          [2] - Listar cadastros
          [3] - Buscar pessoa
          [0] - Sair''')
    
    
def cadastrar():
   dicionario = {}
   dicionario["nome"] = str(input("Digite o seu nome: ")).strip()
   dicionario["idade"] = int(input("Digite a sua idade: "))
   dicionario["email"] = str(input("Digite o seu email: ")).strip()
   while True:
       if "@" not in dicionario["email"] or "." not in dicionario["email"]:
           print("Email inválido")
       else:
           cadastros.append(dicionario)
           break
   

   
def listar():
    if len(cadastros) == 0:
        print("Não há cadastros")
    else:
        for lista in cadastros:
            print(f'Nome: {lista["nome"]}')
            print(f'Idade: {lista["idade"]}')
            print(f'Email: {lista["email"]}')
            
            
def buscar():
    busca = input("Deseja buscar qual usuário? ")
    encontrado = False
    for pessoa in cadastros:
        
        if busca.lower() in pessoa['nome'].lower():
            print(f"Resultado: {pessoa}")
            encontrado = True
    if encontrado == False:
        print("Nâo foi encontrado o sujeito")
        
        
while True:
    Menu()
    
    try:
        opcao = int(input("Digite a sua opcao: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            buscar()
        elif opcao == 0:
            break
        else:
            print("Opção inválida")
    except ValueError:
        print("Seu programa deu erro!")

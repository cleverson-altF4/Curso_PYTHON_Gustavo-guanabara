lista = []

print("*"*40)
print("Menu de compras")
print('''
      [1] - Adicionar um produto
      [2] - Remover um produto
      [3] - Mostrar a lista de compras
      [4] - sair da lista''')
opcao = int(input("Selecione uma opção: "))

while True:
    
    if opcao == 1:
        produto = str(input("produto: ")).strip()
        if produto == '':
            print("produto vazio não é permitido")
        elif produto in lista:
            produto("O produto está na lista")
        else:
            lista.append(produto)
            print("O produto foi adicionado na lista.")
    elif opcao == 2:
        produto = str(input("Qual produto deseja remover? ")).strip()
        
        if produto in lista:
            lista.remove(produto)
            print("Produto removido")
        else:
            print("Produto não encontrado")
    elif opcao == 3:
        print("\nLista de compras")
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            for posicao, compras in enumerate(lista):
                print(f"{posicao + 1} = {compras}")
    elif opcao == 4:
        print("\nLista de compras completa")
        for posicao, compras in enumerate(lista):
            print(f"{posicao + 1} = {compras}")
    else:
        print("Opção inválida")


   
        


    

lista = []

while True:
    print("*"*40)
    print("~"*12, "Lista de compras", "~"*12)
    print('''
        [1] - Adicionar produto na lista
        [2] - Remover o produto da lista
        [3] - Mostrar os produtos da lista
        [4] - Sair do programa''')
    opcao = int(input("Selecione a opção desejada: "))
    
    if opcao == 1:
        produto = str(input("Nome do produto da lista: ")).strip()
        
        if produto == '':
            print("\nNão é permitido espaços vazios")
        elif produto in lista:
            print("O produto está na lista")
        else:
            lista.append(produto)
            print("\nProduto adicionado com sucesso!")

    elif opcao == 2:
        produto = str(input("Qual produto deseja remover? ")).strip()
        
        for posicao, mercadoria in enumerate(lista):
            if mercadoria == produto:
                print("\nRemovendo produto da lista")
                lista.remove(mercadoria)
                print(f"{posicao + 1} = {mercadoria} removido ")
                break
        else:
            print("Este produto não está na lista")

    elif opcao == 3:
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            for posicao, mercadoria in enumerate(lista):
                print(f"{posicao + 1} = {mercadoria}")

    elif opcao == 4:
        print("\nTabela completa da lista de compras\n")

        if len(lista) == 0:
            print("A lista está vazia")
        else:
            for posicao, mercadoria in enumerate(lista):
                print(f"{posicao + 1} = {mercadoria}")
                break
        
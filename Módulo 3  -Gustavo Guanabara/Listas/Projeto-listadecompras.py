"""Lista de compras interativa"""


lista = []
def Menu():
    print("*"*50)
    print('''
        [1] - Adicionar produto na lista
        [2] - Remover o produto da lista
        [3] - Mostrar os produtos da lista
        [4] - Sair do programa
    ''')
    print("*" * 50)


def escolher(opcao):
    if opcao == 1:
        produto = str(input("adicione um produto: ")).strip()
        if produto == '':
            print("Não é permitido espaços")
        elif produto in lista:
            print("O produto está na lista")
        else:
            lista.append(produto)
            print("Produto registrado")
    elif opcao == 2:
        produto = str(input("Qual produto deseja remover")).strip()

        for indice, mercadoria in enumerate(lista):
            if mercadoria == produto:
                print(f"Removendo {produto}")
                lista.remove(mercadoria)
            else:
                print("Não há item para remover")
    elif opcao == 3:
        print("===== Produtos da lista ====")
        for indice, mercadoria in enumerate(lista):
            print(f"{indice+1}: {mercadoria}")


while True:
    Menu()
    try:
        opcao = int(input("Selecione a opção desejada: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao == 4:
        print("\nTabela completa da lista de compras\n")
        for posicao, mercadoria in enumerate(lista):
            print(f"{posicao + 1} = {mercadoria}")
        break

    escolher(opcao)
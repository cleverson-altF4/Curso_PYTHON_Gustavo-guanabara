valor_um = 0
valor_dois = 0
opcao = 0
somar = 0
multi = 0

while opcao != 4:
    print('''
    1 - somar
    2 - multiplicar
    3 - novos números
    4 - sair do programa
    ''')

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        valor_um = int(input("Valor 1: "))
        valor_dois = int(input("Valor 2: "))
        somar = valor_um + valor_dois
        print(f"{valor_um} + {valor_dois} = {somar}")

    elif opcao == 2:
        valor_um = int(input("Valor 1: "))
        valor_dois = int(input("Valor 2: "))
        multi = valor_um * valor_dois
        print(f"{valor_um} x {valor_dois} = {multi}")

    elif opcao == 3:
        valor_um = 0
        valor_dois = 0
        print("Números reiniciados!")

    elif opcao == 4:
        print("Saindo do programa...")

    else:
        print("Opção inválida!")

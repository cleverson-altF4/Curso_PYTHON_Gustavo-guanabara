import time

numero_1 = int(input("Valor 1: "))
numero_2 = int(input("Valor 2: "))
opcao = 0

while opcao != 5:
    print('''
      [1] - soma
      [2] - Multiplicação
      [3] - Maior
      [4] - Novos números
      [5] - sair do programa''')
    opcao = int(input("Selecione uma opção: "))
    
    if opcao == 1:
        soma = numero_1 + numero_2
        print(f"{numero_1} + {numero_2} = {soma}")
    elif opcao == 2:
        produto = numero_1 * numero_2
        print(f"{numero_1} x {numero_2} = {produto}")
    elif opcao == 3:
        if numero_1 > numero_2:
            maior = numero_1
        else:
            maior = numero_2
            print(f"Entre o {numero_1} e {numero_2} o maior número é {maior} ")
    elif opcao == 4:
            print(" ~ ~ ~ ~ Digite novamente ~ ~ ~ ~")
            numero_1 = int(input("Valor 1: "))
            numero_2 = int(input("Valor 2: "))
    elif opcao == 5:
            
            tempo = time.sleep(1)
            print('Saindo em 3...')
            tempo = time.sleep(1)
            print("Saindo em 2...")
            tempo = time.sleep(1)
            print("Saindo em 1...")


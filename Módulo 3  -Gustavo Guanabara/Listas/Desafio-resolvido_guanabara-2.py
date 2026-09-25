from xxlimited_35 import Str

listaNumeros = []

while True:
    numero = int(input("Digite um número: "))
    if numero not in listaNumeros:
        listaNumeros.append(numero)
        listaNumeros.sort()
        print(f"Número {numero} adicionado")
    else:
        print("Este número está na lista")
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim ou Nao]: ")).strip().upper()
        if continuar == '':
            print("\nEspaço em branco. digite novamente\n")

        else:
            continuar = continuar[0]
    if continuar == 'N':
        break

#Crie um programa onde o usuario possa digitar vários números e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicinado.
#No final serão exibidos todos os valores únicos digitados em ordem crescente

lista = []

while True:
    numero = int(input("Digite um número: "))
    if numero in lista:
        print("Esse número está na lista")
    else:
        lista.append(numero)
        print("Adicionado com sucesso!")
        
        
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim ou Nao]: ")).strip().upper()
        if continuar == '':
            print("ERRO!")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
            
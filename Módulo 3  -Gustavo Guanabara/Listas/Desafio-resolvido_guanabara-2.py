#Crie um programa onde o usuario possa digitar vários números e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicinado.
#No final serão exibidos todos os valores únicos digitados em ordem crescente
numeros = []

while True:
    num = int(input("Digite um número: "))
    
    if num not in numeros:
        numeros.append(num)
        numeros.sort()
        print("valor adicionado com sucesso!")
    else:
        print(f"Números duplicados")

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim ou Nao]: ")).strip().upper()
        if continuar == '':
            print("\nEspaço em branco. digite novamente\n")
            
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print(f"Números dos valores = {numeros}")
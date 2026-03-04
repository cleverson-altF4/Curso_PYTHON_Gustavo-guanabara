lista = []

while True:
    dicionario = {}
    dicionario["Nome"] = str(input("Digite o seu nome: ")).strip()
    dicionario["idade"] = int(input("Digite a sua idade: "))
    lista.append(dicionario)
    
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim ou Nao]: ")).strip().upper()
        if continuar == '':
            print("\nEspaço em branco. digite novamente\n")
            
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
for pos in lista:
    print(pos)
print()
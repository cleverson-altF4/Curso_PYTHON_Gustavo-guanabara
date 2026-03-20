lista = []
soma_idade = 0
total_mulheres = 0
while True:
    pessoa = {}
    pessoa['Nome'] = str(input("Digite o seu nome: ")).strip() 
    pessoa['Sexo'] = str(input("Digite o seu sexo: [M/F]: ")).strip().upper()
    pessoa['idade'] = int(input("Digite a sua idade: "))
    while pessoa['Sexo'] not in ['M', 'F']:
        print("Digite corretamente apenas [M ou F]")
        pessoa['Sexo'] = str(input("Digite novamente: ")).strip().upper() [0]
        
    #Unir a lista e dicionário
    lista.append(pessoa.copy())
    
    total = len(lista)
    soma_idade += pessoa['idade']
    media = soma_idade / len(lista)
    
    if pessoa['Sexo'] == 'F':
        total_mulheres += 1
    
    
    continuar = str(input("Deseja continuar? "))[0]
    if continuar == 'n':
        break

print(f"Total de pessoas: {total} ")
print(f"A média de idade: {media:.2f}")
print(f"Total de mulheres: {total_mulheres}")

        
      
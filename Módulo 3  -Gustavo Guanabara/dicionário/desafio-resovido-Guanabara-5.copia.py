pessoa = {} # dicionário
galera = [] # lista
soma = media = 0


#Entrada de dados
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Nome: ")).strip()
    
    while True:
        pessoa['Sexo'] = str(input("Sexo: ")).upper()[0]
        
        if pessoa['Sexo'] in 'MF':
            break
        print("Digite o sexo corretamente")
        
    galera.append(pessoa.copy())

        
    pessoa['idade'] = int(input("Digite a sua idade: "))
    soma += pessoa['idade'] # Soma todas as idades
    
    while True:
        resposta = str(input("Deseja continuar: digite [Sim ou Não]: ")).upper()[0]
        
        if resposta in 'SN':
            break
        print("Digite apenas [Sim ou Não]")
        
    if resposta == 'N':
        break
    
print("-"*35)
print(galera)

print(f"A - Ao todo foram {len(galera)} pessoas")

media = soma / len(galera)

print(f"B - A média de todas as idades: {media:5.2f} anos")


print(f"Uma lista de todas as mulheres cadastradas foram", end= ' ')

for i in galera:
    if i['Sexo'] in 'Ff':
        print(f"{i['Nome']}", end= ' ')
    

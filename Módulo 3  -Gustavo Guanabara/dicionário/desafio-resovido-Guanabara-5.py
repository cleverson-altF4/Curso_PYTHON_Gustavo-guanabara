#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.

#No final mostre:
# A - Quantas pessoas foram cadastradas

# B - A média de idade 

# C - Uma lista com mulheres

# D - Uma lista com idade acima da média

pessoa = {}
galera = []
soma = media = 0

while True:
    pessoa.clear() #Limpa o buffer
    pessoa['nome'] = str(input("Digite o seu nome: ")).strip()
    
    #Valida se o sexo está corretamente e se não ele vira loop até digitar corretamente
    while True:
        pessoa['sexo'] = str(input("Digite o seu sexo: [M ou F]: ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print("Apenas M ou F")
    #Valida a entrada de idade         
    while True:
        idade = input("Digite a sua idade: ")
        
        if idade.isdigit():
            pessoa['idade'] = int(idade)
            break
        else:
            print("Apenas números")
            
    galera.append(pessoa.copy()) #cópia 
    
    soma += pessoa['idade'] #Soma todas as idades digitados
            
    while True:
        resposta = str(input("Deseja continuar? aperte [S/N]: ")).upper()[0]
        if resposta in 'SN':
            break
        print("Erro! tente novamente")   
        
    if resposta == 'N':
        break

print("-"*35)
print(f"A - Ao total foram cadastrados {len(galera)} pessoas")
media = soma / len(galera)
print(f"B - Média de idades do grupo {media} anos")
print("C - Quantidade de mulheres cadastradas: ", end=' ')

#laço para pegar a quantidade de mulheres
for pessoa in galera:
    if pessoa['sexo'] == 'F':
        print(f"{pessoa['nome']}", end= ' | ')
print()
    
print("-"*35)

#Laço para pegar a média

for pessoa in galera:
    if pessoa['idade'] >= media:
        print("  ", end='')
        for keys, valor in pessoa.items():
            print(f"{keys}: {valor} ", end= ' | ')
print()
            
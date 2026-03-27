pessoa = {} # dicionário
galera = [] # lista
soma = media = 0

# Entrada de dados
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Nome: ")).strip()
    
    while True:
        pessoa['Sexo'] = str(input("Sexo: ")).upper()[0]
        
        if pessoa['Sexo'] in 'MF':
            break
        print("Digite o sexo corretamente")
    
    pessoa['idade'] = int(input("Digite a sua idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())  # ← movido para depois de coletar a idade
        
    while True:
        resposta = str(input("Deseja continuar: digite [Sim ou Não]: ")).upper()[0]
        
        if resposta in 'SN':
            break
        print("Digite apenas [Sim ou Não]")
        
    if resposta == 'N':
        break
    
print("-" * 35)
print(galera)

print(f"A - Ao todo foram {len(galera)} pessoas")

media = soma / len(galera)

print(f"B - A média de todas as idades: {media:5.2f} anos")

print("-" * 30)
print("     Mulheres registradas     \n")
print("C - ", end='')
for i in galera:
    if i['Sexo'] == 'F':  # ← corrigido
        print(f"{i['Nome']}", end=' | ')

print("\nD - Lista de pessoas que estão acima da média:")
for i in galera:
    if i['idade'] >= media:
        print()
        for keys, valor in i.items():  # ← corrigido
            print(f"   {keys}: {valor}")
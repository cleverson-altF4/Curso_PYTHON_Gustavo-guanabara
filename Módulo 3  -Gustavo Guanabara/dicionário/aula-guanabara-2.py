#Laços
pessoas = {'nome': 'Clevison', 'idade': 31, 'sexo': 'M', 'Nacionalidade': 'Brasil'}

#------------------------------
pessoas['nome'] = 'Cuca'

#----------------------------
pessoas['peso'] = 74

for chaves in pessoas:
    print(f"{chaves}:")
    
print("-"*50)

for chaves in pessoas.keys():
    print(chaves)
    
print("-"*50)

for chaves in pessoas.values():
    print(chaves)
    
print("-"*50)

for chaves in pessoas.items():
    print(chaves)
    
print("-"*50)

#Em vez de usar enumerate usa-se assim
for chaves, valores in pessoas.items():
    print(f"{chaves}: {valores}")

print("-"*50)


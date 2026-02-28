#dicionarios

#Criando uma estrutura 
pessoas = { 
    'Nome': 'Clevison',
    'Idade': 31,
    'Sexo': "M"
} 

#Alterando o nome da estrutura criada
pessoas['Idade'] = 30


#Adicionando items no dicionário
pessoas['Profissao'] = 'Futuro Dev'


#removendo um item usando Del ou pop
del pessoas['Idade']
pessoas.pop("Sexo")


#Percorrendo um dicionário apenas chaves
for chaves in pessoas:
    print(chaves)
print()
    
#percorrendo chaves e valores
for chaves, valores in pessoas.items():
    print(chaves, ':' , valores)
print()







estado = {}
brasil = []

for i in range(2):
    estado['Uf'] = str(input("Unidade Federativa: ")).strip()
    estado['sigla'] = str(input("Sigla: ")).strip()
    brasil.append(estado.copy())
    
for estado in brasil:
    for posicao, valor in estado.items():
        print(f"{posicao}: {valor}")
    print("-"*30)
    
    
for estado in brasil:
    for posicao in estado.values():
        print(f"{posicao}", end= ' ')
    print()
    
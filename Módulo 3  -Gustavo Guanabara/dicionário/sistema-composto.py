#Lista + Dicionário (Muito importante 
pessoa = [
    {'nome': 'Clevison Rocha Silva', 'idade': 31},
    {'nome': 'Cleiton Rocha silva', 'idade': 24},
    {'nome': 'Claudia Gualberto da Rocha', 'idade': 30},
    {'nome': 'Luana Santos Porto', 'idade': 27},
    {'nome': 'Fulano', 'idade': 10}
]
    
for lista in pessoa:
    print(f"Nome: {lista['nome']} | idade: {lista['idade']} anos")
    if lista['idade'] >= 18:
        print(f"Maiores de idade: {lista['nome']}")
        
    else:
        print(f"Menores de idade: {lista['nome']}")

    

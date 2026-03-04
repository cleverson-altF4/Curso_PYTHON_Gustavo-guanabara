#revisão


pessoa = {
    "Nome": "Clevison Rocha Silva",
    "idade": 31
}

#Condição
if pessoa["idade"] >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
    
#Laço For    
for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')
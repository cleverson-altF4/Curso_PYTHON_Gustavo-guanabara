produtos = (
    'Sabão', 1.40,
    'Arroz tio João',5.40,
    'Arroz Dalon', 34.50,
    'Feijão Carioca', 6.40,
    'Macarrão 1Kg', 3.50,
    'Frango inteiro o kg', 26.15,
    'Linguiça Toscana', 20.51,
    'Linguiça calabresa suína', 15.50,
    'Abóbora', 15.20
     
)

print("*"*40)
print("~"* 10,"Lista de produtos", "~"* 10)
print("*"*40)
print()

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f"{nome:.<30} R$: {preco:>6.2f}")
    


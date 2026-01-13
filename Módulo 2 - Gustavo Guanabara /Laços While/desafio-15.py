#crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. no final mostre

# qual é o total gasto na compra
# quantos produtos custam mais de R$ 1000 reais
# Qual é o nome do produto mais barato
total_gasto = 0
produto_mais_barato = 0
preco_do_produto_mais_barato = 0
usuario = 0
mais_de1000 = 0
contador = 0
print("*"* 50)
print()
print('*'*10, "Mercadinho do jaca", '*'*10)
print()
while True:
    nome_produto = str(input("Qual é o nome do produto: ")).strip().upper()
    preco = float(input("Qual é o preço do produto: "))
   
    print()
    print("*"* 50)
    
    
    
    total_gasto += preco
    contador += 1
    
    if preco > 1000:
        mais_de1000 += 1
    
    if contador == 1 or preco < preco_do_produto_mais_barato:
        preco_do_produto_mais_barato = preco
        preco_do_produto_mais_barato = nome_produto
        
    usuario = str(input("Deseja continuar? [Sim ou Não]: ")).strip().upper()[0]
    if usuario == 'N':
        break
        
print(f"Total do valor gasto: R$ {total_gasto}")
print(f"Valor do produto mais caro: R$ {mais_de1000} reais")
print(f"O produto mais barato: {preco_do_produto_mais_barato}")
    
  
    
    
       
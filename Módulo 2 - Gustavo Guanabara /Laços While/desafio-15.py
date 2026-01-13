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
    
    total_gasto += preco # variável que soma os valores dos produtos
    contador += 1 # Contador que irá comparar todos os produtos somados
   
    if preco > 1000:
        mais_de1000 += 1
        
    if contador == 1 or preco < preco_do_produto_mais_barato: 
        # se o contador pegar o número 1 ele irá comparar vários produtos 
        # se o preço do produto for menor que a variável do produto mais barato
        preco_do_produto_mais_barato = preco
        #pega a variável do preço mais barato e compara ao preço do produto
        produto_mais_barato= nome_produto
        #variável do produto mais barato ele compara qual o produto é o menor preço
        

    usuario = str(input("Deseja continuar? [Sim ou Não]: ")).strip().upper()[0]
    if usuario == 'N':
        break
        
print(f"Total do valor gasto: R$ {total_gasto}")
print(f"Temos {mais_de1000} produto com mais de MIl reais")
print(f"O produto mais barato: {produto_mais_barato}")
    
  
    
    
       
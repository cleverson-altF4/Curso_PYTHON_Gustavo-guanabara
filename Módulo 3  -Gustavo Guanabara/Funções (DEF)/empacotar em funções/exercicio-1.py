#Crie uma função que receba vários números e retorne a soma deles
def numeros(*soma):
    print("-"*25)
    res = sum(soma)
    print(f"A soma total dos números {soma} é {res}")
      
numeros(1,2,3)
numeros(2,2,6)

input("\nClick enter: ")


#Faça uma função que receba vários números e mostre qual é o maior
def numero(*maior):
    print("-"*25)
    resultado = max(maior)
    print("O maior número {}: {}".format(maior,resultado))
    

numero(2,4,6,8,10)
numero(3,1,3,5)

input("\nClick enter: ")

#Crie uma função que receba vários valores e diga:
#Quantos números foram passados
#A soma
#A média

def linha():
    print("-"*25)
    
    
linha()   
def quantidadeNumeros(*valores):
    print(f"Total de números {len(valores)}")
    soma = sum(valores)
    print(f"A soma total dos valores {soma}")
    
    media = sum(valores) / len(valores)
    print(f"A média dos números: {media:.2f}")
    
    
quantidadeNumeros(2,5,3,6,4,8)
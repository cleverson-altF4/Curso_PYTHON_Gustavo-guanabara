#Números somados 

valores = []

def numeros_somados(numero):
    posicao = 0
    
    while posicao < len(numero):
        numero[posicao] += 1
        posicao += 1
        
        
        
numeros_somados(valores)
print(valores)

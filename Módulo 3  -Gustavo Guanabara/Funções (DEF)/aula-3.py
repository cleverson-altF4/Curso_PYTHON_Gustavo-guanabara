valores = [1,2,3,4,5,6,7,8,9,10]

def dobra_valor(lista):
    posicao = 0
    
    while posicao < len(lista):
         lista[posicao] *= 2
         posicao += 1
    
    

dobra_valor(valores)
print(valores)


#praticar essa lógica
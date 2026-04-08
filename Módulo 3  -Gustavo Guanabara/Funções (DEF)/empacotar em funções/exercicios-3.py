#Multiplicador

#Faça uma função que receba vários números e um multiplicador fixo:

def multiplicador(*numero, fator=6):
    resultado = []
    
    for num in numero:
        resultado.append(num * fator)
        print(resultado)
    
        
        
multiplicador(4,8,16,32)
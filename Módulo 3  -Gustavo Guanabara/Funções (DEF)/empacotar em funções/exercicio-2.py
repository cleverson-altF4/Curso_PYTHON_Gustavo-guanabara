#Crie uma função que receba várias notas e retorne:
#Quantidade de notas
#Maior nota
#Menor nota
#Média

#Extra: opção para mostrar ou não a situação (aprovado/reprovado).

def linha():
    print("-"*25)
    
    

def numero(*notas, sintuacao=False):
    quantidade = len(notas)
    
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / quantidade
    
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    
    if sintuacao:
        if media >= 7.5:
            print("Aprovado")
        
        else:
            print("Reprovado")
    
    
    
    
numero(2,1,5,10,15) # Não mostra a sintuação
linha()
numero(2,5,3,4,5,9,7,3, sintuacao=True) #Mostra a sintuação
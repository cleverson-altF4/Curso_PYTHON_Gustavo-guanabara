print("-"*40)
print("-"*15, "Lotofácil", "-"*15)

from random import randint

Cartela = []
todas_as_cartelas = []

quantidade = int(input("Quantas cartelas deseja: "))

total = 1

while total <= quantidade:
    contador = 0
   
    while contador < 15:
        numeros = randint(1, 25)
        
        if numeros not in Cartela:
            Cartela.append(numeros)
            contador += 1
            
    #Ordenação Manual   (Buble Sort)     
    for i in range (len(Cartela)):
        for j in range (i + 1, len(Cartela)):
            if Cartela[i] > Cartela[j]:
                temporaria = Cartela[i]
                Cartela[i] = Cartela[j]
                Cartela[j] = temporaria
        
    todas_as_cartelas.append(Cartela[:])
    Cartela.clear()
    total += 1
    
for i in range(len(todas_as_cartelas)):
    print(f"{i + 1}: {todas_as_cartelas[i]}")
            

        
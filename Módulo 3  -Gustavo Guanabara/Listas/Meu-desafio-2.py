lista = []

while True:
    numero = int(input("Digite um número: "))
    
    if numero not in lista:
        lista.append(numero)
    
        
       
    continuar = str(input("Deseja continuar?")).strip().upper()[0]
    if continuar == 'N':
        break
    
print(lista)
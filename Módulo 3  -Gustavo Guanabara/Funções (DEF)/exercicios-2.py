def media(numero):
    print("-"*30)
    if not numero:
        return 0
    else:
        return sum(numero) / len(numero)
    

lista_numero = []
par = impar = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    
    lista_numero.append(numero)
    
    
    
    
for numero in range(len(lista_numero)):
    if numero % 2 == 0:
        print(f"Números pares: {numero}")
        par += 1
    else:
        print(f"Números ímpares: {numero}")
        impar += 1
        

print(f"A média dos números citados foram: {media(lista_numero):.2f}")
print(f"A quantidade de números pares: {par}")
print(f"A quantidade de números ímpares: {impar}")


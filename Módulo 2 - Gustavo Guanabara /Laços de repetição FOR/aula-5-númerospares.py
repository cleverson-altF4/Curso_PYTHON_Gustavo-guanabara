soma = 0
contador = 0
for numero in range(1, 7):
    num = int(input("Digite de 1 à 7: "))
    if num % 2 == 0:
        print(f"{num} e par")
        soma += num
        contador += 1
    else:
        print(f"{num} ìmpar")
        soma += num
        contador += 1
    
print("Soma total = {}".format(soma))


    
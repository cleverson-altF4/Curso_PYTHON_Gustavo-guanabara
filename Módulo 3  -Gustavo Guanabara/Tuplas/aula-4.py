valores = (
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: "))
 )
print(f"A = O 9 apareceu {valores.count(9)} vezes")
if 3 in valores:
    print(f"B = O 3 apareceu na posição {valores.index(3) + 1}")
else:
    print("O número 3 não foi digitado")
   
    
print("C = Números pares:", end=" ")
for par in valores:
    if par % 2 == 0:
        print(par, end= ' ')
        
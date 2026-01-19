valores = (
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: "))
)

print("Você digitou os valores {}".format(valores))
if 9 in valores:
    print(f"Contem o 9 em {valores.count(9)}x")
else:
    print("Não foi digitado o 9")
    
    
if 3 in valores:
    print(f"O 3 ficou na posição {valores.index(3)+ 1}")
else:
    print("O 3 não foi digitado.")
    
  
print(f"Números pares: ", end= '')  
for par in valores:
    if par % 2 == 0:
        print(par, end= '-')
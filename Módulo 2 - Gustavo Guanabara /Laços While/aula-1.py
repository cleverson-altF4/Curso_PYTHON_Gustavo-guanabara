numero = 1
par = impar = 0

while numero != 0:
    numero = int(input("Digite um valor se é par ou ímpar: "))
    if numero % 2 == 0:
        par += 1
    else: 
        impar += 1
        
print("\033[0m Números pares:", f"\033[33m {par}")
print("\033[0m Números ímpares:", f"\033[33m {impar}")
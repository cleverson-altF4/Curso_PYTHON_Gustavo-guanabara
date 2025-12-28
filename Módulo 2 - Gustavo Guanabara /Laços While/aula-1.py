valor = 's'
par = impar = 0
while valor == 's':
    numero = int(input("Digite um valor: "))
    valor = str(input("\nquer continuar s/n: ")).lower()
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Números pares {par}")
print(f"Números ímpares {impar}")
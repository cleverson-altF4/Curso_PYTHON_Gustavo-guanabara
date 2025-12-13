nu1 = int(input("Primeiro número: "))
nu2 = int(input("Segundo número: "))

if nu1 > nu2:
    print(f"\33[1;33m{nu1} é maior que {nu2}")
elif nu1 < nu2:
    print(f"\33[1;33m{nu1} é menor que {nu2}")
else:
    print("Números são iguais")
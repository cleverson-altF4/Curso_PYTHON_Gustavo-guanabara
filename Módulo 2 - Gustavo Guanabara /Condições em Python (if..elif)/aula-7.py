a = float(input("Lado A "))
b = float(input("Lado B "))
c = float(input("Lado c "))

if a + b > c and a + c > b and b + c > a:
    print("Formam um triângulo")
    if a == b == c:
        tipo = 'Equilátero'
    elif a == b or a == c or b == c:
        tipo = 'Isosceles'
    else:
        tipo = 'Escaleno'
    print(f"Tipo = {tipo}")
else:
    print("Não forma um triângulo")
    tipo = 'Não está correto'
    print("Tipo = {}".format(tipo))


a = float(input("valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de B: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c


menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"Números digitados A = {a}, B = {b} e C = {c}")
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")

if a == b == c:
    print("Todos os números são iguais")
elif a > b < c:
    print(f"A = {a} maior que B = {b} e menor que C = {c}")
elif a > c < b:
    print(f"A = {a} maior que C = {c} e menor que  B = {b}")
elif c > a > b:
    print(f"C {c} é maior que A = {a} e maior B = {b}")
elif c > a < b:
    print(f"C = {c} é maior que A = {a} e menor que B = {b}")
elif c < b > a:
    print(f"C = {c} menor que B = {b} e maior que A = {a}")
else: 
    print("Me perdi kkk")
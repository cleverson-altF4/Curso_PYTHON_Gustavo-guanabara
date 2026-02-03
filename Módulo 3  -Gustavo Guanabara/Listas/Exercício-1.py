numeros = []
soma = 0

for i in range(5):
    num = float(input(f"digite um número de {i + 1} = "))
    numeros.append(num)
    soma += num
    
    
print(f"Lista = {numeros}")
print(f"Soma = {soma:.2f}")



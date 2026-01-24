a = [1, 2, 3, 4]
b = a
b[2] = 0 # isso ocorre quando uma lista está interligada a outra e nisso ambos mudam por iguais
print(f"Lista A: {a}")
print(f"Lista B: {b}")

print("*"* 21)

a = [1, 2, 3, 4]
b = a[:] #cópia e nisso os valores mudarão
b[2] = 0 # isso ocorre quando uma lista está interligada a outra e nisso ambos mudam por iguais
print(f"Lista A: {a}")
print(f"Lista B: {b}")
from random import randint

numeros = (
    randint(1,5),
    randint(1,5),
    randint(1,5),
    randint(1,5),
    randint(1,5),
)
print(numeros)
print(f"Menor número {min(numeros)}")
print(f"Maior número: {max(numeros)}")
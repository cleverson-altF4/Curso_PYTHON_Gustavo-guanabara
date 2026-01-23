from random import randint

numeros = (
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10),
)

for n in numeros:
    print(f"{n}", end= ' ')
print()
print(f"O maior número {max(numeros)}") 
print(f"O menor número {min(numeros)}")
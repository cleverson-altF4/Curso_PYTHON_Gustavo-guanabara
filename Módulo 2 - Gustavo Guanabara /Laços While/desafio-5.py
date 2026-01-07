primeiro_termo = int(input("Progressão aritmética: "))
razao = int(input("Razão: "))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f"{termo} -> ", end= ' ')
    termo = termo + razao
    contador += 1
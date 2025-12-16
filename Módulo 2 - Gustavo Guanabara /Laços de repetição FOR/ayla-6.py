primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("De quanto em quanto? "))
P_a = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, P_a + razao, razao):
    print(f"{i}", end= ' ')
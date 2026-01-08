primeiro_termo = int(input("Progressão aritmética, digue um número: "))
razao = int(input("Razão: "))
termo = primeiro_termo
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <=  total:
        print(f"{termo}", end= ' - ')
        termo = termo + razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos vocẽ quer mostrar a mais? "))
print("Total de termos finalizados {}".format(total))
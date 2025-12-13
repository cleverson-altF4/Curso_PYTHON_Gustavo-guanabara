viagem = float(input("Qual distância é o percurso? "))
print("### Viagem ####\n")

if viagem <= 0:
    print("Não é tem distância")
elif viagem < 200:
    preco = viagem * 0.50
    print(f"A viagem será de {viagem} km")
    print(f"O valor a ser pago será R$ {preco:.2f} reais")
else:
    preco = viagem * 0.45
    print(f"O Percurso será de {viagem} km")
    print(f"O valor a ser pago será de R$ {preco:.2f} reais")
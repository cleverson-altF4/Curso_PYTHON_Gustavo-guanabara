total_vendas = 0
tota_desconto = 0
compras_acima_100 = 0

AMARELO = "\033[33m"

print("#"*10,'Loja de compras', "#"*10)
for i in range(1, 6):
    print(f"\nCompra - {i}")
    compra = float(input("Digite o valor da compra: "))

    if compra > 200:
        desconto = compra * 20/100
        compras_acima_100 += 1
        print(f"O valor da compra foi de R$ {compra:.2f} reais")
        print(f"Desconto de R$ {desconto:.2f}")
    elif compra > 100:
        desconto = compra * 10/100
        print(f"O valor da compra foi de R$ {compra:.2f} reais")
        print(f"Desconto de R$ {desconto:.2f} reais")
    else:
        desconto = 0
        print(f"O valor da compra foi de {compra:.2f} reais")
        print("Não há desconto no valor abaixo de R$ 100 reais")


Final = compra - desconto
total_vendas += Final
tota_desconto += desconto

print("\n" + "*"*50)
print(f"{AMARELO}Valor final da compra foi de {Final:.2f} reais")


print("\n~******** Relatório *******~\n")
print(f"Total de vendas: {total_vendas:.2f}")
print(f"Total de descontos em cada compra: {tota_desconto:.2f} reais")
print(f"Total de vendas acima de R$ 200: {compras_acima_100}")

if total_vendas > 500:
    print("Bateu a meta. Parabéns")
else:
    print("Não bateu a meta")
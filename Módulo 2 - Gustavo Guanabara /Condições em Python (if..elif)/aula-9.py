print('{:*^50}'.format(" Supermercado do Jaca "))
compra = float(input("Qual o valor da compra: R$ "))
print(''' Formas de pagamento
[1] Pagamento á vista em dinheiro ou cheque.
[2] Pagamento à vista no cartão de crédito.
[3] parcelado no cartão de crédito em 2x.
[4] Parcelado no cartão de crédito em 3x ou mais.''')

opcao = int(input("Qual é a forma de pagamento: "))

if opcao == 1:
    print("O pagamento realizado sem juros")
    print(f"O valor da compra foi de R$ {compra:.2f} reais")
    valor = compra - (compra * 10 / 100)
    print("O valor do desconto á vista será de 10%")
    print(f"O valor da compra foi de R$ {valor:.2f} reais")
elif opcao == 2:
    print("Pagamento á vista no cartão sem júros")
    print(f"O valor da compra foi de R$ {compra:.2f} reais")
    valor = compra - (compra * 5 /100)
    print(f"O Valor da compra foi de R$ {valor:.2f} reais")
elif opcao == 3:
    print("O pagamento parcelado em 2x terá 5% de júros.")
    valor = compra + (compra * 5 / 100)
    parcela = valor / 2
    print(f"O valor da compra será de {valor:.2f}")
    print(f"total parcelado será de R$ {parcela:.2f} reais")
else:
    valor = compra + (compra * 20 / 100)
    quantidade_parcelas = int(input(("Quantas parcelas: ")))
    parcela = valor / quantidade_parcelas
    print("O pagamento parcelado em 3x ou mais terá um acréscimo de 20% de júros")
    print(f"O valor da compra foi de R$ {compra:.2f} reais")
    print(f"O valor parcelado em {quantidade_parcelas}x foi de R$ {parcela:.2f} reais")
valor_casa = float(input("Qual o valor da casa: "))
salario = float(input("Quanto você ganha: "))
anos = int(input("Em quantos anos você vai pagar: "))
prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100

if valor_casa <= minimo:
    print(f"O valor da casa é de R$ {valor_casa:.2f}")
    print(f"O tempo em anos será de {anos} anos")
    print(f"O valor da prestação será de R$ {prestacao:.2f} reais")
else:
    print("Negado!")
salario = float(input("Quanto você ganha? "))

if salario <= 1250.00:
    minimo = salario * 0.15
    total = salario + minimo
    print(f"O valor atual é de R$ {salario:.2f} reais")
    print(f"O valor do seu salário ajustado de 15% é de R$ {minimo:.2f} reais")
    print(f"O total do valor recebido será R$ {total:.2f} reais")
else:
    maximo = salario * 0.10
    total = salario + maximo
    print(f"O seu salário atual é de R$ {salario:.2f} reais")
    print(f"O seu valor ajustado com o aumento de 10% é de R$ {maximo} reais")
    print(f"O total do salário será de R$ {total:.2f} reais")
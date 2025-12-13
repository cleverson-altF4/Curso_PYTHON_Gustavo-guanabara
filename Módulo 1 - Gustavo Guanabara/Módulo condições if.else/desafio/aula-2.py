carro = float(input("Qual a velocidade do carro: "))
print("### CNH ####\n")

if carro > 80:
    acima = carro - 80
    multa = acima * 7
    print("A velocidade do carro é {} km/h".format(carro))
    print(f"O carro estava acima de {acima} Km/h")
    print(f"A multa será de {multa} por Km rodado")
else:
    print("Você está dentro do limite de velocidade")
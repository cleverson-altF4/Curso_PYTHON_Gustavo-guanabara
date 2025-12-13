num = int(input("Digite: "))
if num <= 0:
    print("Número 0 não é permitido")
else:
    unidade = num // 1 % 10 
    dezena = num // 10 % 10
    centena = num // 100 % 10
    milhar = num // 1000 % 10

    print(f"Unidade {unidade}")
    print(f"dezena {dezena}")
    print(f"centena{centena}")
    print(f"milhar {milhar}")   
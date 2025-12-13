numero1 = float(input("\33[1;33mDigite uma nota:" ))
numer2 = float(input("\33[1;33mDigite outra nota" ))
media = (numero1 + numer2) / 2
if media <= 0:
    print(f"A sua média é de {media:.2f} = Reprovado")
elif media < 3:
    print(f"A sua média é {media:.2f} = Recuperação")
elif media < 6:
    print(f"A sua média é de {media:.2f} = Boa")
elif media < 8:
    print(f"A sua média é de {media:.2f} = Ótimo")
else:
    print("Você é fodão e atingiu o limite máximo da nota")

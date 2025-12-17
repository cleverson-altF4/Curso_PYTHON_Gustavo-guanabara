frase = str(input("Digite algo: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print(inverso)
if inverso == junto:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
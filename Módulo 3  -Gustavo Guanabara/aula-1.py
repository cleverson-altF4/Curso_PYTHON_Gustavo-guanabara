numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
while True:
    tabela = int(input("Digite um número de [0 à 20]: "))
    if 0 <= tabela <=20:
        break
    else:
        print("Tente novamente")

print(f"Você digitou o número: {numeros[tabela]}")
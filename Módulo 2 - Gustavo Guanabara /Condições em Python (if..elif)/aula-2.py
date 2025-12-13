numero = int(input("Digite um número em inteiro para Binário: "))
print('''
Número
[1] Binário
[2] Octal
[3] Hexadecimal''')

opcao = int(input("Qual seria? "))

if opcao == 1:
    print(f"{numero} para binário {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} para Octal {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} para Hexadecimal {hex(numero)[2:].upper()}")
else:
    print("ERRO! tente novamente.")
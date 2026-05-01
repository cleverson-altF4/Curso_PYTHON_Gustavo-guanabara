print("Sem tratamentos de erros\n")

numero = int(input("Digite um número: "))
print(10 / numero)

input("\n")


print("Com tratamento de erros\n")
try:
    print("Vai dá erro")
except:
    numero = int(input("Digite um número: "))
    print(10 / numero)
    
    
input("\n")


print(" Exemplo simples\n")
try:
    numero = int(input("Digite um valor"))
    print(10 / numero)
except:
    print("Deu ruim")
    
    
input("\n")

print("Tratando erros específicos (forma correta)\n")
try:
    numero = int(input("Digite um valor"))
    print(10 / numero)
except ValueError:
    print("O número que você digitou não está correto")
except ZeroDivisionError:
    print("Número não é divisivel por Zero")
    
input("\n")

print("Estrutura completa\n")

try: 
    numero = int(input("Digite um valor: "))
except ValueError:
    print("Erro de valor")
else:
    print("Tudo ok, continue")
finally:
    print("Fim do programa")
    
    

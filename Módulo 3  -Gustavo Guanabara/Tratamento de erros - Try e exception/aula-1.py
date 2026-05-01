#  Sem tratamentos de erros

numero = int(input("Digite um número: "))
print(10 / numero)

input("\n")


#  Com tratamento de erros
try:
    print("Vai dá erro")
except:
    numero = int(input("Digite um número: "))
    print(10 / numero)
    
    
input("\n")


#  Exemplo simples
try:
    numero = int(input("Digite um valor"))
    print(10 / numero)
except:
    print("Deu ruim")
    
    
input("\n")

#  Tratando erros específicos (forma correta)
try:
    numero = int(input("Digite um valor"))
    print(10 / numero)
except ValueError:
    print("O número que você digitou não está correto")
except ZeroDivisionError:
    print("Número não é divisivel por Zero")
    
    

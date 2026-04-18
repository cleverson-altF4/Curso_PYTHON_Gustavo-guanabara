def fatorial(numero=1):
    fat = 1
    
    for i in range(numero, 0, -1):
        fat *= i
    return fat

num = int(input("Digite um número fatorial: "))
print(f"O número {num} fatorial dele é {fatorial(num)}")

input("\nEnter: ")

#----------------------------------------------------------------
def par(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False
    
nume = int(input("Digite um número: "))
if par(nume):
    print("Par")
else:
    print("ìmpar")



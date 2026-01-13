valor_saque = 0
print("*"*50)
print('~'* 15, "Banco central", '~'* 15)
print("*"*50)
while True:
    dinheiro = int(input("Quanto quer sacar: "))
    
    if dinheiro <= 100:
        print("\nO valor do saque será dividido em 2 cédulas de R$ 50,00\n")
        
        
    if dinheiro <= 0:
        print("\n\033[31mErro!\033[mNão podemos sacar valores inferiores\n")
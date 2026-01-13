#interrompendo fluxo repetições While com flag
numero = soma = quantidade = 0
while True:
    numero = int(input("Digite um número: "))
    
    if numero == 999:
        break
    
    soma += numero
    quantidade += 1
print(f"A soma = {soma}")
print(f"Quantidade de números = {quantidade}")
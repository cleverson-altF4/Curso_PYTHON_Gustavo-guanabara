lista = []

while True:
    numero = int(input("Digite um valor: "))
    
    if numero in lista:
        print("Não aceitamos números repetidos.")
    else:
        lista.append(numero)
        
    usuario = ''
    while usuario not in ('S', 'N'):
        usuario = str(input("Deseja continuar? [Sim ou Não]")).strip().upper()
        if usuario == '':
            print("Não aperte enter")
        else:
            usuario = usuario[0]
    if usuario == 'N':
        break

print("*"*40)
print(f"Números digitados = {lista}")
print(f"Maior número = {max(lista)}")
print(f"Menor número = {min(lista)}")
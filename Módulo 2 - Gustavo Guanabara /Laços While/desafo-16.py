
print("*"*50)
print('~'* 15, "Banco central", '~'* 15)
print("*"*50)

dinheiro = int(input("Sacar valor R$: "))
total = dinheiro
cedulas = 50
total_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        print(f"Total de {total_cedulas} células de R$ {cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if total == 0:
            break
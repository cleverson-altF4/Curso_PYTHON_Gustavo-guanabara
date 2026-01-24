valores = []
valores.append(0)
valores.append(1)
valores.append(2)

for v in valores:  # posso usar o básico
    print(f"{v}-")
    
print("*"* 30)

for i, v in enumerate(valores): # Ou usar com uma numeração e saber a posição de cada
    print(f"posição {i} - {v}")

print("*"*30)

for contador in range(0,5): # ou posso usar esse usando uma quantidade de vezes adicionado em valores vazios dentro do for e usando input
    valores.append(int(input("Digite um valor: [1 à 5]: ")))
    print(f"Valores adicionados {valores}")


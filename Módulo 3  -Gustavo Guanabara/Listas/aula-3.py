valores = []
valores.append(0)
valores.append(1)
valores.append(2)

for v in valores:  # posso usar o básico
    print(f"{v}-")
    
print("*"* 30)

for i, v in enumerate(valores): # Ou usar com uma numeração e saber a posição de cada
    print(f"posição {i} - {v}")

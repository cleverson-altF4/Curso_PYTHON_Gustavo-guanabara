soma = subtracao = multi = divisao = resultado = 0
while True:
    tabuada = int(input("Tabuada: "))
    
    for i in range(11):
        soma = tabuada + i
        resultado = soma
        print(f"{tabuada} + {i} = {resultado}")
    
    print("\nDeseja continuar? \n")
    continuar = int(input("Sim/Não: ")).strip().upper()[0]
    if continuar == 'S':
        continue
    else:
        break
        
        
    

        
        
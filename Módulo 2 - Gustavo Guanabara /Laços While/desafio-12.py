soma = resultado = 0
while True:
    tabuada = int(input("Tabuada: "))
    if tabuada <= 0:
        break
    
    
    for i in range(11):
        soma = tabuada * i
        resultado = soma
        print(f"{tabuada} x {i} = {resultado}")
    
print("\nEncerrando o programa\n")    

    
        
        
    

        
        
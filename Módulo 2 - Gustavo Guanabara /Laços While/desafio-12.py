soma = resultado = 0
while True:
    tabuada = int(input("Tabuada: "))
    if tabuada <= 0:
        print("\n\033[31mErro!\033[m")
        break
    
    
    for i in range(11):
        soma = tabuada * i
        resultado = soma
        print(f"{tabuada} x {i} = {resultado}")
    if i > 11:
        break
    
print("\nEncerrando o programa\n")    

    
        
        
    

        
        
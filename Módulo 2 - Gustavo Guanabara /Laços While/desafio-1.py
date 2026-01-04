#Faça um programa que leia o sexo, mas so aceite os valores "M" ou "F", caso contrário
#peça a digitação novamente até ter um valor correto

contador = 0

while True:
    entrada = str(input("Digite seu sexo [M] ou [F]: ")).strip()
    if not entrada:
        print("entrada vazia. tente novamente")
        contador += 1
        continue
        
    sexo = entrada[0].upper()
    
    if sexo in ('M', 'F'):
        break
    print("Dados inválidos, digite apenas 'M ou F")
    contador += 1
        
        
print(f"Sexo [{sexo}] registrado")
if contador:
    print(f"Teve {contador} tentativas")

    
        
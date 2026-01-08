while True:
    primeiro_termo = int(input("Progressão aritmética: "))
    razao = int(input("Razão: "))
    contador = 1
    
    termo = primeiro_termo
    contador = 0
    
    print(f"{termo}")
    
    while contador < 10:
        termo = termo + razao
        contador += 1
        print(f"{termo}", end= ' - ')
          
    print("\n")
    
    continuar = str(input("Deseja continuar? S/N ")).strip().upper()
    
    if continuar == 'N':
        print("Foram contadas {} vezes".format(contador))
        break
    
    
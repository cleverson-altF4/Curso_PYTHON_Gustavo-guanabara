def leiaInt(msg, valor = 0, validacao = False):
    
    while True:
        n = str(input(msg))
        
        if n.isnumeric():
            valor = int(n)
            validacao = True
        else:
            print("\033[0;31mERRO! tente apenas números inteiros\033[m")
            
        if validacao:
            break
    return valor

n = leiaInt("Digite um número: ")
print(f"Você digitou: {n}")
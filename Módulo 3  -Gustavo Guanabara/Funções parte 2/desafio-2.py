def fatorial(numero=1, show=True):
    """
        parâmetro: numero=1
        parâmetro: show=False
        
        for i para numero da função, até 0 e -1 para voltar de trás para frente  
            dentro do for uma condição if show:
                if posição I > 1:
                    mostra "x", end= '' para cada i selecionado
                    
                if posição i == 1:
                    mostra "=" antes do resultado 
        return fat = fatorial ja multiplicado
    
    """
    fat = 1
    
    for i in range(numero, 0, -1):
        fat *= i
        if show: 
            print(f"{i}", end='')
            if i > 1:
                print("x", end='')
                
            if i == 1:
                print("=",end='')
    return fat
        
        
        


numer = int(input("Digite um número fatorial: "))
print(fatorial(numer, show=True))

help(fatorial)


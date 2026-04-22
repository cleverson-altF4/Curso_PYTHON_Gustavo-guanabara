#tupla para pegar as cores do ANSI

cores = ['\033[31m', '\033[32m', '\033[m']


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print("~"* tamanho) 
    print(f"  {msg}  ")
    print("~"* tamanho) 
    print(cores[2])
    
    

    
        

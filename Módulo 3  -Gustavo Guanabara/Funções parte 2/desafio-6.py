#interactive Help()
cores = (
    "\033[33m", #posição 0 - amarelo
    "\033[37m", #posição 1 - Branco
    "\033[31m", #posição 2 - Vermelho
    "\033[m",   #posição 3 - apaga a cor
)

def ajuda(com):
    titulo(f"Acessando o manual do comando {com}",1)
    print(cores[1])
    help(com)
    print(cores[3])

    
def titulo(msg, cor=0):
    print(cores[cor], end='')
    tamanho = len(msg) + 4
    print("-"*tamanho) 
    print(  msg)
    print("-"*tamanho)
    print(cores[3], end='') 

#Programa principal
while True:
    titulo("Sistema de ajuda PYHELP",0)
    comando = str(input(">>> ")).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
titulo("Até logo", 2)
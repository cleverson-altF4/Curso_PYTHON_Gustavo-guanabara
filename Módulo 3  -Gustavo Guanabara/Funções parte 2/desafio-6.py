from time import sleep

cores = ['\033[31m', '\033[32m', '\033[m']
fundo_verde = ['\033[42m']

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print("-"* tamanho) 
    print(f"  {msg}  ")
    print("-"* tamanho) 
    print(cores[2]) 
    sleep(1)  
    
def ajuda(com_ajuda):
    titulo(f"Acessando o manual do comando {com_ajuda}", cor=1 )
    print(fundo_verde[0], end='')
    help(com_ajuda)
    print(cores[2])
    
while True:
   titulo("SISTEMA DE AJUDA PYHELP", cor=0)
   
   usuario = input(">>> ").strip()
   if usuario.lower() == 'fim':
       titulo("Projeto concluído", cor=1)
       break
   else:
       ajuda(usuario)
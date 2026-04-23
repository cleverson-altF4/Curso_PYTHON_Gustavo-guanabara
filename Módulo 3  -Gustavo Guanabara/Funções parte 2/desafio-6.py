#tupla para pegar as cores do ANSI

cores = ['\033[31m', '\033[32m', '\033[m']

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print("~"* tamanho) 
    print(f"  {msg}  ")
    print("~"* tamanho) 
    print(cores[2])   
    
def ajuda(com_ajuda):
    print(cores[1])
    titulo(f"Acessando o manual do comando {com_ajuda}", cor=1 )
    help(com_ajuda)
    print(cores[2])

while True:
   titulo("SISTEMA DE AJUDA PYHELP", cor=0)
   
   usuario = input(">>> ").strip()
   if usuario.lower() == 'fim':
       break
   else:
       print(cores[2])
       ajuda(usuario)
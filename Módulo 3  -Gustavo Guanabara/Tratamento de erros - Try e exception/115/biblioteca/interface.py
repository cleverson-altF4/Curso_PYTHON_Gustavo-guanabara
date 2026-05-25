def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print("Erro!Digite um número inteiro válido")
        except KeyboardInterrupt:
            print("Usuário preferiu digitar esse número")
            return 0
        else:
            return numero
        

def linha(tamanho=42):
    return "-" * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
   
    
    
def menu(lista):
    cabecalho("Menu Principal")
    
    contador = 1
    
    for i in lista:
        print(f"\033[33m{contador}\033[m = \033[34m{i}\033[m")
        contador += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
    
        
    
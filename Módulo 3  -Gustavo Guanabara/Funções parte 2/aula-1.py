#interative help()
#Docstrings
#argumentos opcionais
#escopo de variáveis
#retorno de resultados

#aula de hoje é sobre interative help()
#----------------------------------------------------------------------------
#interative help()
#No terminal usei o python3 e depois coloquei help() em sequida usei todo o recurso para saber sobre a documentação do python
#>>> help() ou 
# 2º opção --  help(print)
#3º opção -- print(input.__doc__) >> Não recomendado 
#-----------------------------------------------------------------------------



#Aula de hoje é sobre Docstrings
#------------------------------------------------------------------------------

def contador(inicio, fim, passo):
    """
    Realiza uma contagem do número inicial até o número final,
    incrementando conforme o passo informado.

    Args:
        inicio (int): Início da contagem.
        fim (int): Final da contagem.
        passo (int): Incremento entre os números.
    """
    print("\nO uso do Docstrings\n")
    cont = inicio
    
    while cont < fim:
        print(cont, end=' ')
        cont += passo
    print("fim")
        
        
contador(1,11,1)
#print(help(contador))


input("\nEnter: ")

#aula de hoje é sobre parâmetros opcionais
#----------------------------------------------------------------------------



def somar(a=0,b=0,c=0):
    soma = a + b + c
    print(f"A soma vale {soma}")
    
somar(2,1,4) #chamada com as 3 opções
somar(1,2) #Chamada com 2 opções porém c = 0
somar(1) #Chamada com 1 opção
somar() #Chamada vazia mas o meu argumento mostra que tenho a,b,c = 0
somar(a=10, b= 10)

input("\nEnter: ")



#aula de hoje é sobre Escopo de variáveis
#----------------------------------------------------------------------------

def teste():
   #n = 8
    x = 1 #Local
    print(f"No programa dentro N = {n}")
    print(f"No programa dentro X = {x}")

n = 2 # Global
print(f"No programa fora N = {n}")
teste()

input("\nEnter: ")
#-----------------------------------------------------------------------------

def testan(b):
    print("\n Sem o uso do global")
    a = 8 # duas váriveis - um local e outro global
    b += 4
    c = 2
    print(f"A = dentro vale {a}")
    print(f"B = dentro vale {b}")
    print(f"C = dentro vale {c}")
    #escopo local


a = 5
testan(a)
print(f"A = fora vale {a}")
#Escopo global

input("\nEnter: ")

#---------------------------------------------------------------------------
def testando(b):
    print("\\n Usando o global\n ")
    global a # o escopo fora fica sendo o alvo principal e o local apaga
    a = 8 # duas váriveis - um local e outro global
    b += 4
    c = 2
    print(f"A = dentro vale {a}")
    print(f"B = dentro vale {b}")
    print(f"C = dentro vale {c}")
    #escopo local


a = 5
testando(a)
print(f"A = fora vale {a}")

input("\nEnter: ")

#Escopo global
#------------------------------------------------------------------------------

def funcao():
    n1 = 4
    print(f"N1 dentro vale {n1}")

#programa principal

n1 = 2
print(f"N1 fora vale {n1}")
funcao()

input("\nEnter: ")


#aula de hoje é sobre Retorno de valores
#----------------------------------------------------------------------------

def somando(a=0, b=0, c=0):
    print("Com limitação, sem o uso do return")
    
    resultado = a + b + c
    print(f"Resultado = {resultado}")
    

somando(3,5,1) #Sem o uso do return eu não poderia chamar a função mais de 1x

input("\nEnter: ")
#---------------------------------------------

def somatoria(A=0, B=0, C=0):
    
    soma = A + B + C
    return soma

resposta1 = somatoria(1,2,3)
resposta2 = somatoria(2,2)
resposta3 = somatoria(A=2, B= 3, C=5) #Nesse caso eu posso chamar a função várias vezes
print("\nCom o uso do return")
print(f"Resposta 1 = {resposta1}")
print(f"Reposta 2 = {resposta2}")
print(f"Resposta 3 = {resposta3}")

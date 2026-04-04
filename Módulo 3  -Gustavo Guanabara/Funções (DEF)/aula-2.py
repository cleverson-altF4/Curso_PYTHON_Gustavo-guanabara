#Função com o nome soma e tem como parâmetro (a,b)
def soma(a, b):
    print("-"*10)
    print(f"A = {a} e B = {b}")
    res = a + b 
    print(f"A soma total de A + B = {res}")


#Esse aqui chama a função
soma(3, 4)
input("\nDigite enter...")

#______________________________________________________________

#Multiplicação
def multiplica(a, b):
    print(f"{a} * {b}")
    return a * b


resultado = multiplica(2, 3)
print(resultado)
input("\nDigite enter...")

#_______________________________________________________________


def saudacao(nome='Visitante'):
    print(f"{nome} está aprendendo funções em python")
    
    


saudacao() #Padrão visitante
saudacao('Clevison') #Nome selecionado para o parâmetro
input("\nDigite enter...")


#_______________________________________________________________


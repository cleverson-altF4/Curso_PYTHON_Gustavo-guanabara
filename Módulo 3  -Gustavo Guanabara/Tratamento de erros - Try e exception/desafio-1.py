def leiaInt(msg): 
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
            print(f"Erro! digite um número inteiro válido")
        else:
             return numero
         
        
def leiaFloat(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except ValueError:
            print("Erro! Digite um número decimal válido")
        else:
            return n
            
   

num = leiaInt("digite um número: ")
a = leiaFloat("Digite um número decimal: ")
print(f"Resultado: Número inteiro {num} | Número Real {a}")
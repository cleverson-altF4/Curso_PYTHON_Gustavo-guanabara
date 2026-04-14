#Lição de hoje — Tratamento de Erros 
# No drone isso é crítico. Se um sensor falhar, o programa não pode travar — ele precisa tratar o erro e continuar funcionando com segurança


#Se o arquivo não existir, o programa trava e para tudo
import json


#1 - sem o try/Except
with open("log.json", "w") as arquivo:
   dados = json.load(arquivo)
    
    
#2 - Com o Try/Except
try:
    with open("log.json", "r") as arquivo:
        dados = json.load(arquivo)
    print("Log carregado")
except FileNotFoundError:
    print("Arquivo não encontrado")
    
    
#3 - Com múltiplos erros
try:
    altitude = int(input("Digite a altitude: "))
    resultado = 100 / altitude
except ValueError:
    print("Digite um número válido!")
except ZeroDivisionError:
    print("Altitude não pode ser zero!")
    
    
#4 - Bloco finally sempre executa
try:
    with open("log.json", "r") as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    print("Verificação concluída.")
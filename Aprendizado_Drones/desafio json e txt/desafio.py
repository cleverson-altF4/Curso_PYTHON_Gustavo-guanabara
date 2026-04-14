import json
import time

drone = {
    "nome": "Drone-01",
    "bateria": 20,
    "altitude": 160
}


#Salva os dados no json
def salvar_log(drone):
    with open("log.json", "w") as arquivo:
        json.dump(drone,arquivo)
        
    
#Carregar log
def carregar_log():
    with open("log.json", "r") as arquivo:
        dados = json.load(arquivo)
        return dados
   
#registranod evento
def registrar_evento(mensagem):
    with open("log.txt", "a") as arquivo:
        arquivo.write(f"Adicionando: {mensagem} \n")
        
        
salvar_log(drone)

resultado = carregar_log()

for i, valor in enumerate(resultado.items()):
    print(f"{i+1}: {valor}")
    
    
registrar_evento("Evento concluído")
registrar_evento("Aprendizado sobre .txt e .json")
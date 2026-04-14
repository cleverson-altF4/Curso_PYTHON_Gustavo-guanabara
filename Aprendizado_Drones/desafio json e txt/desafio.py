import json

drone = {
    "nome": "Drone-01",
    "altitude": 89,
    "bateria": 30
}

def salvar_log(drone):
    with open("log.json", "w") as arquivo:
        json.dump(drone,arquivo)
         
         
def carregar_log():
    with open("log.json", "r") as arquivo:
        dados = json.load(arquivo)
        return dados
    
def registrar_evento(mensagem):
    with open("log.txt","a") as arquivo:
        arquivo.write(mensagem + "\n")
        
salvar_log(drone)
    
dados = carregar_log()
print(dados)

registrar_evento("Decolagem iniciada")


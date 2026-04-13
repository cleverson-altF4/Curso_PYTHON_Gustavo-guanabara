import json
from time import sleep

with open("Relatório.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Iniciando um voo\n")
    
    
with open("Relatório.txt", "r") as arquivo:
    aberto = arquivo.read()
    print(aberto)
    
    
with open("Relatório.txt", "a") as arquivo:
    arquivo.write("Adicionando dados\n")
    
        
drone = {
    "nome": "Drone-1",
    "bateria": 70,
    "Voando": True,
    "altitude": 80
}

with open("Drone.json", "w") as arquivo:
    json.dump(drone, arquivo)
    
    
with open("Drone.json", "r") as arquivo:
    abrir_json = json.load(arquivo)
    
for i, leitura in abrir_json.items():
    print(f"{i}: {leitura}")
    sleep(1)
    
    

import json


drone = {
    "nome": "Drone-01",
    "bateria": 40,
    "altitude": 80,
    
}

def salvar_log(drone):
    try:
        with open("log.json", "w") as arquivo:
            json.dump(drone, arquivo)
    except Exception as e:
        print(f"Erro ao salvar: {e}")
        
    
def carregar_log():
    try:
        with open("log.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print("Ñão foi encontrado nenhum arquivo")
    finally:
        print("\n\033[33mVerificação concluída\033[0m\n")
        
        
salvar_log(drone)

dados = carregar_log()
print(dados)
    
        

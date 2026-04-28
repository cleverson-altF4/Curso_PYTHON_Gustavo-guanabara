altitude = 0
ciclo = 0
direcao = 1


def status_drone(altitude, direcao=1):
    if direcao == 1 :
        status = "Subindo"
    else:
        status = "Descendo"
        
    print(f"Altitude = {altitude}m | {status}...")
    
    
def verificar_bateria(bateria):
    if bateria >= 50:
        print(f"BATERIA OK: {bateria}%")
    elif bateria >= 20:
        print(f"BATERIA BAIXA: {bateria}% ")
    else:
        print(F"ALERTA 🚨: RETORNAR IMEDIATAMENTE! {bateria}%")
        
        
print("==== RELATÓRIO DO DRONE =====")
status_drone(3.5)
verificar_bateria(80)
print("="*29)
print()

print("==== RELATÓRIO DO DRONE =====")
status_drone(1.2, direcao=-1)
verificar_bateria(15)
print("="*29)

    
    
    

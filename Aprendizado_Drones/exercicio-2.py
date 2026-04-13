# Lista de altitudes planejadas para uma missão

altitude = [10,35,40,30,58,12]

print(altitude[0])
print(altitude[-1])
print(len(altitude))

altitude.append(11)
altitude.insert(1,5)
altitude.remove(10)
altitude.remove(40)
altitude.remove(58)

for alti in altitude:
    print(f"Próximo maxpoint: {alti}m")
    

input("\n Enter :")

#Dicionário com nome


drone = {
    'Altitude': 35.5,
    'Bateria': 78,
    'Velocidade': 12.3,
    'modo': 'Automático'
}

print(drone['Altitude'])
drone['Bateria'] = 45
drone['Temperatura'] = 25

for chave, valor in drone.items():
    print(f"{chave}: {valor}")
    
    
input("\n Enter: ")

Drone = {
    'nome': 'Clevison Rocha Silva',
    'altitude': 150,
    'Em_voo': True, 
    'Bateria': 20
}
    
def exibir_status(Drone):
    
    for keys,mostrar in Drone.items():
        print(f"{keys}: {mostrar}")
        

historico_altitudes = []
historico_altitudes.append(150)
historico_altitudes.append(300)
historico_altitudes.append(400)


def altitude_maxima(historico_altitudes):
    return max(historico_altitudes)


exibir_status(Drone)
maior = altitude_maxima(historico_altitudes)
print(f"Altitude máxima: {maior}")





    
    

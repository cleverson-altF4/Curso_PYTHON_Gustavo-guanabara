def dec(altitude):
    print(f"Subirá para {altitude} metros")
    return altitude

dec(20)


def decol(altitud=30, pouso=0.5):
    print(f"A altura necessária: {altitud} metros")
    print(f"O pouso será de {pouso} segundos")
    return altitud, pouso
    
    
decol()

def posicao():
    x = 10
    y = 15
    z = 7
    
    return x,y,z

pos_x, pos_y, pos_z = posicao()
print(f"A posição de X: {pos_x}")
print(f"A posição de Y: {pos_y}")
print(f"A posição de Z: {pos_z}")


def decolagem(altitude):
    print(f"Decolagem {altitude}")
    

def pousar():
    print("Pouso")
    
    
def status_bateria(percentual):

    if percentual > 20:
        return 'Ok'
    else:
        return 'Baixa'
        
    



decolagem(20)
pousar()
status = status_bateria(15)
print(status)
        
    




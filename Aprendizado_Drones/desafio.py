import time
import math
import random

def simular_voo(segundos):
    
    for leitura in range(segundos):
        altitude = random.uniform(10, 100)
        print(f"Leitura {leitura + 1}: {altitude:.2f}")
        time.sleep(1)
        
        

def distancia_ate_a_base(pontoX, pontoY):
    calculo = math.sqrt(pontoX**2 + pontoY**2)
    return calculo
    
    
simular_voo(4)
resultado = distancia_ate_a_base(15,30)
print(f"A distância da base: {resultado}m")
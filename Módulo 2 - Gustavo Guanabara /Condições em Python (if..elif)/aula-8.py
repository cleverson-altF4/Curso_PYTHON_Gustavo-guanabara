peso_kg = float(input("Qual é o seu peso: "))
altura = float(input("Qual é a sua altura: "))
imc = peso_kg / altura**2
print(f" Imc calculado = {imc:.2f}")
if imc < 18.5:
    classificacao = 'Magreza'    
elif imc >= 18.5 and imc < 25:
    classificacao = 'Normal'
elif imc >= 25 and imc < 30:
    classificacao = 'Sobrepeso'
elif imc >= 30 and imc < 35:
    classificacao = 'Obesidade 1'
elif imc >= 35 and imc < 40:
    classificacao = 'Obesidade 2'
else:
    classificacao = 'Obesidade 3 - Mórbido'

print(f"Peso = {classificacao}")
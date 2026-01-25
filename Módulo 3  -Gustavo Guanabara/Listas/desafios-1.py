#Faça um programa que leia 5 valores numericos e guarde-as em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista  
valores = []

for contador in range(0, 5):
    valores.append(int(input("Digite valor de 1 à 5: ")))

print("*" * 40)

maior = max(valores)
menor = min(valores)
print(f"Os valores digitados foram os valores {valores}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

print("*" * 40)

for posicao in range(0, len(valores)):
    print(f"{posicao}-  posição {valores[posicao]}")
    
    if valores[posicao] == maior:
        print(f"O maior número está está na {posicao}")
        
    if valores[posicao] == menor:
        print(f"O menor número está na posição {posicao}")
        
print("*"*40)
#Faça um programa que tenha uma função chamada area() que receba as dimensoes de um terreno retangular largura e comprimento e mostre a área do terreno
def linha():
    print("    \nControle de terrenos")
    print("----------------------")
    
linha()
largura = float(input("Largura m²: "))
comprimento = float(input("Comprimento m²: "))

def area(largura, comprimento):
    valor = largura * comprimento
    print(f"A aŕea de um terreno é {largura} x {comprimento} é de {valor:.2f} m²")
    
 
area(largura, comprimento)

    
    


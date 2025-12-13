#Definir a lista de palavras e o limite N.
#Inicializar contador e lista de resultados vazios.
#Percorrer cada palavra com for.
#Usar if para testar se len(palavra) > N.
#Se verdadeiro, incrementar contador e adicionar a lista.
#Ao final, imprimir contador e lista.

lista_palavras = ["Casa", "Amoeba", "Abacate", "Computador", "Sabonete"]
limite = 4
contador = 1
lista = []
for list_palavras in lista_palavras:
    if len(list_palavras) > limite:
        contador += 1
        lista.append(list_palavras)

print(f"Quantidade: {contador}")
print("palavras maiores que ", limite, "caractere", lista)
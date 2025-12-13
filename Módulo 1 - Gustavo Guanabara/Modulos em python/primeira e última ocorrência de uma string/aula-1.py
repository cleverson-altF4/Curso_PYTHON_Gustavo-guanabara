frase = str(input("Digite uma frase: ")).strip().upper()
print(f"Quantas vezes a palavra (A) aparece? {frase.count('A')}")
print(f"Em que posição ele aparece na primeira vez? {frase.find('A') + 1}")
print(f"Em que posição ele aparece na última? {frase.rfind('A') + 1}")

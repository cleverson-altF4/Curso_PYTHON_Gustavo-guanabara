frase = 'Clevison gostosao'
print(frase[0:8])  #pega o indíce 0 até o 8 => 'Clevison'

#1. Pegar do início até o meio:
print(frase[:4]) #pega do 0 até o 4 => 'clevi'

#2. Pegar do meio até o fim:
print(frase[4:]) #pega do 4 até o fim => 'ison gostosao'

#3. Usar passo (de 2 em 2):
print(frase[::2]) # pula de 2 em 2 => 'clevison gostoso' => Ceio otso

#4. Inverter o texto:
print(frase[::-1]) #inverte as palavras do fim para o começo.

#5. Pegar últimos caracteres:
print(frase[-8:]) #começa no 8 até o fim.

#6. começa do 1:5:2
print(frase[1:5:2])
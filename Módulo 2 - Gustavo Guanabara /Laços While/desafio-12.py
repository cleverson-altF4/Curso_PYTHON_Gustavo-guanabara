soma = subtracao = multi = divisao = resultado = 0
while True:
    tabuada = int(input("Tabuada: "))
    resultado = soma + tabuada
    for tabuada in range(11):
        print(f"{tabuada} + {soma} = {resultado}")
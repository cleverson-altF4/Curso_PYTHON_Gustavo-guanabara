#máquina de venda de ingressos
#Quantidade de ingressos disponíveis

idade = int(input("Qual é a sua idade: "))

if idade < 12:
    print("Filme com a classificação de 12. (Recomendamos filme infantil) - ")
elif 12 <= idade < 18:
    print("Filme com classificação 16 anos. (Recomendamos filme adolescente) ")
else:
    print("Filme com classificação 18+ (Recomendamos filme para adulto) ")

ingressos = 10
total = int(input("Quantidade de ingressos: "))

if total <= ingressos:
    print("Temos ingressos disponíveis")
else:
    print("Os ingressos esgotaram")
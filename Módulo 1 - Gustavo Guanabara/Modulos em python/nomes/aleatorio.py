#nomes aleatórios 
import random
n1 = input("nome: ")
n2 = input("nome: ")
n3 = input("nome: ")
n4 = input("nome: ")

alunos = [n1, n2, n3, n4]
random.shuffle(alunos)

print(alunos)
#!/usr/bin/env python3
# EXERCÍCIOS PRÁTICOS - SOLUÇÕES COMENTADAS
# Execute para testar!

# Ex1: par_impar
def par_impar(n):
    if n % 2 == 0:
        return 'Par'
    return 'Ímpar'

print(f'4: {par_impar(4)}')  # Par

# Ex2: media
def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

print(f'Média [10,20,30]: {media([10,20,30])}')  # 20.0

# Ex3: fatorial (iterativo)
def fatorial(n):
    if n < 0:
        return 'Erro: negativo!'
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(f'5! = {fatorial(5)}')  # 120

# Ex4: celsius_fah
def celsius_fah(c):
    return (c * 9/5) + 32

print(f'30°C = {celsius_fah(30):.1f}°F')

# Ex5: validador senha
def validar_senha(senha):
    if len(senha) < 6:
        return 'Fraca: curta'
    if not any(c.isupper() for c in senha):
        return 'Fraca: sem maiúscula'
    if not any(c.isdigit() for c in senha):
        return 'Fraca: sem número'
    return 'Forte! ✅'

print(validar_senha('abc123'))  # Fraca: sem maiúscula
print(validar_senha('Abc123'))  # Forte!

print('Todos exercícios OK! 🎉')

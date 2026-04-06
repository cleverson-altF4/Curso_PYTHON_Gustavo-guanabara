#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TUTORIAL PRÁTICO: FUNÇÕES EM PYTHON - PROJETO CALCULADORA INTERATIVA
Nível Iniciante - Execute este arquivo: python tutorial_funcoes.py

Passo a passo construindo funções! Copie/comente para aprender.
"""

# =====================================
# PASSO 2: Funções SEM parâmetros
# =====================================
def linha():
    """Função simples SEM parâmetros - desenha linha"""
    print('=' * 40)

def titulo(msg):
    """Função COM parâmetro default"""
    linha()
    print(msg.center(40))
    linha()

# Teste das funções básicas
titulo('Bem-vindo à Calculadora com Funções!')
print('Passo 2 completo! 👆')

# =====================================
# PASSO 3: Funções com PARÂMETROS e RETURN
# =====================================
def somar(a, b):
    """Soma dois números - usa RETURN"""
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return 'ERRO: Divisão por zero!'
    return a / b

# Teste
print('\nPasso 3: Operações básicas')
print(f'Soma: 10 + 5 = {somar(10, 5)}')
print(f'Divisão: 10 / 2 = {dividir(10, 2)}')

# =====================================
# PASSO 4: Função com PARÂMETRO OPCIONAL (default)
# =====================================
def saudacao(nome='Usuário'):
    return f'Olá, {nome}! Vamos calcular?'

print(f'\nPasso 4: {saudacao()}')
print(f'{saudacao("Clevison")}')

# =====================================
# PROJETO PRINCIPAL: Calculadora Interativa
# =====================================
def calculadora():
    """Função principal - menu interativo"""
    titulo('CALCULADORA PYTHON com FUNÇÕES')
    
    while True:
        print('\nEscolha a operação:')
        print('1 - Somar')
        print('2 - Subtrair')
        print('3 - Multiplicar')
        print('4 - Dividir')
        print('5 - Sair')
        
        op = input('Opção (1-5): ')
        
        if op == '5':
            titulo('Volte sempre! 😊')
            break
        
        if op in '1234':
            try:
                n1 = float(input('Primeiro número: '))
                n2 = float(input('Segundo número: '))
                
                if op == '1':
                    res = somar(n1, n2)
                elif op == '2':
                    res = subtrair(n1, n2)
                elif op == '3':
                    res = multiplicar(n1, n2)
                else:
                    res = dividir(n1, n2)
                
                print(f'Resultado: {res}')
            except ValueError:
                print('Erro: Digite números válidos!')
        else:
            print('Opção inválida!')

# Executa o projeto!
if __name__ == '__main__':
    calculadora()

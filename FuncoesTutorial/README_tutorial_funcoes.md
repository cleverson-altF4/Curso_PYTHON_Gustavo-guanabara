# 🎯 Tutorial Completo: Funções em Python - Nível Iniciante (Estilo Projeto)

Olá! Este tutorial ensina **funções (def)** passo a passo, construindo um **projeto prático: Calculadora Interativa**. 

Vamos do zero ao projeto rodando! Copie os códigos no VSCode e execute `python tutorial_funcoes.py`.

## Passo 1: O que são funções?
Funções são blocos de código reutilizáveis. Em vez de repetir código, criamos uma função e **chamamos** ela quando precisar.

**Por quê usar?**
- Organiza código
- Evita repetição
- Fácil testar/modificar

**Sintaxe básica:**
```python
def nome_da_funcao():
    # código aqui
    print('Hello!')
    
nome_da_funcao()  # chamada
```

## Passo 2: Função SEM parâmetros
Primeiro exemplo simples:

```python
def linha():
    print('=' * 30)

linha()  # Saída: ==============================
```

**Exercício 1:** Crie `titulo(msg)` que imprime linha + msg centralizada + linha.

## Passo 3: Funções COM parâmetros
Parâmetros = valores que a função recebe.

```python
def saudacao(nome):
    print(f'Olá {nome}!')

saudacao('Clevison')  # Olá Clevison!
```

**Tipos:**
- Posicional: `def soma(a, b):`
- Keyword: `soma(b=3, a=2)`
- Default: `def saudacao(nome='Visitante'):`

**Exercício 2:** `dobro(n)` que retorna n*2.

## Passo 4: RETURN vs PRINT
`print` mostra na tela. `return` **devolve valor** para usar depois.

```python
def somar(a, b):
    return a + b  # Devolve resultado

resultado = somar(5, 3)
print(resultado)  # 8
```

## Passo 5: Projeto - Calculadora Interativa!
Execute `tutorial_funcoes.py` para ver funcionando.

Código usa todas lições: funções, params, return, menu while.

**Melhore o projeto:**
- Adicione potência (^)
- Validação melhor
- Histórico de cálculos

## Exercícios Práticos:

**Ex1:** Função `par_impar(n)` retorna 'Par' ou 'Ímpar'.
```python
# Solução:
def par_impar(n):
    if n % 2 == 0:
        return 'Par'
    return 'Ímpar'
print(par_impar(4))  # Par
```

**Ex2:** `media(lista)` calcula média de lista.
```python
# Solução:
def media(lista):
    return sum(lista) / len(lista)
print(media([10, 20, 30]))  # 20.0
```

**Ex3:** `fatorial(n)` (use while/recursão simples).
**Ex4:** Menu de conversão (Celsius/Fahrenheit).
**Ex5:** Validador de senha (força baseada em critérios).

## Escopo de Variáveis
```python
def teste():
    x = 10  # Local
    print(x)

x = 5  # Global
teste()  # 10
print(x)  # 5
```

## Bônus: Lambda (funções anônimas)
```python
dobro = lambda n: n * 2
print(dobro(5))  # 10
```

**Execute o projeto e faça exercícios! Próximo módulo: listas. 🚀**


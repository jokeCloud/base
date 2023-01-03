'''
introdução às funções (def) em python
funções são trechos de código usados para
replicar determinada ação ao longo do seu código
elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico
por padrão, funções python retornam none (nada)
'''


def funcao(a, b, c):
    for _ in range(10):
        print(a, b, c)


funcao('ma', 'oi', 'eai')


def teste():
    return 'oi sou a funcao teste'


print(teste)
print(teste())


def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)
imprimir(7, 8, 9)


def saudacao(nome='John Doe.'):
    print(f'Olá {nome}')


saudacao('Emanuel.')
saudacao('Sabedoria.')
saudacao('Leão da tribo de Judá.')
saudacao()

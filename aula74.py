# exercicios com funções

# crie uma funcao que multiplica todos os argumentos
# não nomeados recebidos
# retorno o total para uma variável e mostre o valor
# da variavel

# crie uma funcao fala se um número é par ou ímpar
# retorne se o número é par ou impar


def multiplica_todos_argumentos(*args):
    total = 1
    for numero in args:
        if numero == 0:
            continue
        total *= numero
    return total


# não inserir "0" (zero) no cálculo.
numeros = 0, 1, 2, 3, 4, 5
primeiro_calculo = multiplica_todos_argumentos(*numeros)
print(primeiro_calculo)


def verifica_par_ou_impar(param):
    if param % 2 == 0:
        print(f'{param}: é par.')
    elif param % 2 == 1:
        print(f'{param}: é impar.')
    else:
        print('Não entendi.')


verifica_par_ou_impar(primeiro_calculo)


def par_ou_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'


print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(4))
print(par_ou_impar(5))
print(par_ou_impar(10))

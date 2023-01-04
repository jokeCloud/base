'''
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

# lembrete de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(f'{x=} {y=} {resto=}')


# def soma(x, y):
#    return x + y


def soma_varios_numeros(*args):
    soma_dos_numeros = 0
    for numero in args:
        soma_dos_numeros += numero
    return soma_dos_numeros


print(soma_varios_numeros(1, 2, 3, 4, 5, 6))

soma_1_2_3 = soma_varios_numeros(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma_varios_numeros(4, 5, 6)
print(soma_4_5_6)

tupla = 1, 2, 3, 4
print(sum(tupla))

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma_varios_numeros(*numeros)
print(outra_soma)

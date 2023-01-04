'''
exercicios
crie funcoes que duplicam, triplica, quadriplicam
o numero recebido como parametro
'''

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
numero = 1


def duplicar_1(*args):
    numeros = []
    for numero in args:
        numeros.append(numero * 2)

    return numeros


print(duplicar_1(*numeros))
print(duplicar_1(numero))


def triplicar_1(*args):
    numeros = []
    for numero in args:
        numeros.append(numero * 3)

    return numeros


print(triplicar_1(*numeros))
print(triplicar_1(numero))


def quadriplicar_1(*args):
    numeros = []
    for numero in args:
        numeros.append(numero * 4)

    return numeros


print(quadriplicar_1(*numeros))
print(quadriplicar_1(numero))


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))

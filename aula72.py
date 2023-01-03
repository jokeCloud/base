'''
retorno de valores das funções (return)
'''


def soma(x, y):
    print('olha')
    print('só')
    print('que')
    print('legal')
    if x > 10:
        return 10, 20
    return x + y


variavel = print('ma oi')
print(variavel is None)

variavel = soma(1, 2)
print(variavel)

variavel = int('1')
print(variavel)

soma1 = soma(1, 0)
soma2 = soma(0, 2)
print(soma1 + soma2)
print(soma(11, 77))

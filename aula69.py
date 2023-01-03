'''
argumentos nomeados e não nomeados em funções python
argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)
'''


def soma(x, y, z):
    print(f'{x=} y={y} {z=}  | x + y + z = {x + y + z}',
          '|', 'x+y+z=', x + y + z)


# argumentos não nomeados
soma(1, 2, 3)
# argumentos nomeados
soma(y=2, x=1, z=4)

print(1, 2, 3, sep='-')

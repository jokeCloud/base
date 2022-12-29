"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(10)
print(numeros)
for numero in numeros:
    print(numero)

numeros = range(5, 10)
print(numeros)
for numero in numeros:
    print(numero)

numeros = range(5, 10, 2)
print(numeros)
for numero in numeros:
    print(numero)

numeros = range(-1, -10, -3)
print(numeros)
for numero in numeros:
    print(numero)

# tabuada do 5
numeros = range(0, 51, 5)
print(numeros)
for numero in numeros:
    print(numero)

"""don't works

letras = range('a', 'z')
print(letras)
for letras in letras:
    print(letras)
"""

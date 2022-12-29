"""
Iterável -> str, range, etc, (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
"""

# tabuada do 9
numeros = range(0, 91, 9)

for numero in numeros:
    print(numero)

texto = iter('johansen')  # 'johansen'.__iter__()
print(texto)

texto_1 = iter('texto')

print(texto_1.__next__())
print(texto_1.__next__())
print(texto_1.__next__())
print(texto_1.__next__())
print(texto_1.__next__())
# print(texto_1.__next__())


# o que o FOR faz:

texto_2 = 'joao'
texto_2_com_iterador = iter(texto_2)

while True:
    try:
        letra = next(texto_2_com_iterador)
        print(letra)
    except StopIteration:
        break

# same result

for letra in texto_2:
    print(letra)

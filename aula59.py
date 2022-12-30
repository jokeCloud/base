"""
split e join com LIST e STR
split - divide uma string
join - une uma string
"""

frase = 'Olá só que coisa interessante.'

lista_palavras = frase.split()

print(frase)
print(lista_palavras)

lista_palavras = frase.split(',')

print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print('oi ', lista_palavras[i].strip())

print(lista_palavras)

"""
split e join com LIST e STR
split - divide uma string
join - une uma string
"""

frase = '   Olá só que   , coisa interessante.    '

lista_frases_cruas = frase.split()

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = '-'.join(lista_frases)

print(frases_unidas)

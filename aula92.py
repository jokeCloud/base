lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y, z)
    for x in range(3)
    for y in range(3)
    for z in range(3)
]

print(lista)

lista = [
    [x for y in range(3)]
    for x in range(3)
]
print(lista)


lista = [
    [(x, letra) for letra in 'joao']
    for x in range(3)
]
print(lista)

"""
listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamentos
métodos úteis
    append - adiciona um item ao final
    insert - adiciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lita
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

#       0    1   2   3
lista = [10, 20, 30, 40]

lista.append('50 tipo diferente')
print(lista)

lista.pop(4)
print(lista)

lista.append(51)
print(lista)

del lista[4]
print(lista)

lista.append(50)
print(lista)

lista.insert(0, 5)
print(lista)

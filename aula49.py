"""
Listas em python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
numero = lista[2]

print(numero * 2)
print(lista[2])

lista_alteravel = [100, 200, 300, 400]

lista_alteravel[2] = 301
print(lista_alteravel)

del lista_alteravel[2]
print(lista_alteravel)

lista_alteravel.append(500)
print(lista_alteravel)

retirado_ultimo_valor = lista_alteravel.pop()
print(lista_alteravel, 'Removido:', retirado_ultimo_valor)

lista_alteravel.pop(2)
print(lista_alteravel)

# desempacotamento em chamadas
# de métodos e funções

string = 'abc'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p, b, *_, ap, u = lista
print(p, u, ap)


for nome in lista:
    print(nome, end='')

print(*lista)
print(*string)
print(*tupla)

salas = [
    #   0        1
    ['Maria', 'Helena', ],  # 0
    #   0
    ['Elaine',],  # 1
    #   0        1          2
    ['João', 'Gustavo', 'Milena', (0, 10, 20, 30, 40)],  # 2
]

print(*salas, sep='\n')

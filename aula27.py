"""
fatiamento de strings
 012345678
 Olá mundo
-987654321
fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[0:4])
print(variavel[4:9])
print(variavel[::2])
print(variavel[:9:3])
print(variavel[0:9:4])
print(variavel[0::2])
print(variavel[4:9:])

# len - length - comprimento
print(len(variavel))
print(variavel[:len(variavel):])
print(variavel[0:len(variavel):])
print(variavel[0:len(variavel):2])  # inicio:fim:passo

# inverter
print(variavel[-1:-len(variavel):-1])
print(variavel[::-1])

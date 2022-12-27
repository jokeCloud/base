# interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'johansen'
preco = 1000.95897643
variavel = '%s, o preço é R$ %.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %x, %04x, %05X' % (15, 15, 15, 15))

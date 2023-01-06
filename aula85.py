# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.


# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set('johansen')
s2 = {'masterson', 1, 2}
print(s1, type(s1))
print(s2, type(s2))


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
s3 = {1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6,
      7, 8, 9, 9}  # set remove dados duplicados
print(s3, type(s3))

# ordenar lista de maneira simples, pode ser necessário ordenar
l1 = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9]
print(l1)
s4 = set(l1)
print(s4)
l2 = list(s4)
print(l2)

s5 = s5 = {1, 2, 3}
print(s5)

a = b = 1
print(a, b)

print(3 not in s5)

for numero in s5:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

s6 = set()
s6.add('johansen')
print(s6)
s6.add(1)
print(s6)
s6.update('Olá mundo')
print(s6)
s6.update(('hello world', 1, 2, 3, 4, 5))
print(s6)
s6.clear()
print(s6)
s6.update(('hello world', 1, 2, 3, 4, 5))
print(s6)
s6.discard(1)
print(s6)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s7 = {1, 2, 3}
s8 = {2, 3, 4}

s9 = s7 | s8
print(s9)

s9 = s7 & s8
print(s9)

s9 = s7 - s8
print(s9)

s9 = s8 - s7
print(s9)

s9 = s7 ^ s8
print(s9)


# exemplo de uso do set

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('parabéns')
        break

    print(letras)

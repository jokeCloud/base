"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'johansen'
noutra_variavel = nome
nome = 'joão'

print(nome)
print(noutra_variavel)

lista_a = ['johansen', 'masterson']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

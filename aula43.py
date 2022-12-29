texto = 'python'

i = 0
tamanho_texto = len(texto)

while i < tamanho_texto:
    print(texto[i], i)
    i += 1
"""
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')
"""

frase = 'Muito python'

for letra in frase:
    print(letra)

arr = ['a', 'b', 'c']

for valor in arr:
    print(valor)


linguagem = 'Python'

novo_texto = ''
for letra in linguagem:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

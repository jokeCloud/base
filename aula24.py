# operadores in e not in
# string são iteráveis
#  0 1 2 3 4 5 6 7
#  j o h a n s e n
# -8-7-6-5-4-3-2-1

nome = 'johansen'
print(
    nome[0], nome[1], nome[2], nome[3],
    nome[4], nome[5], nome[6], nome[7]
)
print(
    nome[-1], nome[-2], nome[-3], nome[-4],
    nome[-5], nome[-6], nome[-7], nome[-8]
)

print('joh' in nome)
print('han' in nome)
print('sen' in nome)
print('nse' in nome)

frase = input('Digite uma frase: ')
busca = input('Qual palavra na frase quer buscar? ')

if busca in frase:
    print(f"{busca=}, está em '{frase}' ")
else:
    print(f'Não encontrado {busca=}')

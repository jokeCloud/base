# iterando strings com while
# 0123456789
nome = 'johansen masterson'  # iteráveis
#                -1

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nome_upper = nome.upper()


contador = 0
novo_nome = ''
while contador < tamanho_nome:
    novo_nome += '*'
    novo_nome += nome_upper[contador]
    contador += 1

novo_nome += '*'
print(novo_nome)

RESULTADO_ESPERADO = '*J*O*H*A*N*S*E*N* *M*A*S*T*E*R*S*O*N*'
print(RESULTADO_ESPERADO)

"""
nome = 'johansen masterson'
tamanho_nome = len(nome)
nome_upper = nome.upper()

indice = 0
novo_nome = ''

while indice < tamanho_nome:
    letra = nome_upper[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
"""

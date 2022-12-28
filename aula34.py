"""
repretições
while (enquanto)
executa uma ação enquanto um condição for verdadeira
"""
condicao = 0

while condicao < 10:
    print(f'oi {condicao}')
    condicao += 1

condicao_1 = True

while condicao_1:
    nome = input('Digite seu nome ou aperte enter para sair: ')
    if nome:
        print(f'Seu nome é {nome}')
    else:
        condicao_1 = False

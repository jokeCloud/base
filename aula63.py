"""
operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('valor' if True else 'Outro valor')
print('valor' if False else 'Outro valor')

condicao = 10 == 10

variavel = 'valor' if condicao else 'Outro valor'

print(variavel)


digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if True else 'Outro valor' if True else 'Fim')

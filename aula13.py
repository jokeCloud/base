nome = 'Johansen'
sobrenome = 'Masterson'
altura = 1.90
peso = 110
imc = peso / altura ** 2

'f-strings'
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Johansen Masterson tem 1.90 de altura,
# pesa 110 quilos e seu imc é
# 19.320987654320987

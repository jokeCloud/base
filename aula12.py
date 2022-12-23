nome = 'Johansen'
sobrenome = 'Masterson'
altura = 1.90
peso = 110


def calcula_imc(peso, altura):
    imc = peso / altura ** 2
    return imc


print(f'{nome} {sobrenome} tem {altura:.2f}, pesa {peso} quilos e seu IMC é: {calcula_imc(peso, altura):.2f}')  # noqa

# Johansen Masterson tem 1.90 de altura,
# pesa 110 quilos e seu IMC é
# 19.320987654320987

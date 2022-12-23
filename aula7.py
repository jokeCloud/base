# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáeis com letras minúsculas, pode user
# números e underline _ para palavras compostas
# O sinal de = é operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = exrpessão

nome_completo = 'Johansen Masterson'
soma_dois_mais_dois = 2 + 2
int_um = int('1')

print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois)

nome = 'João'
idade = 19
maior_de_idade = idade >= 18


def traduz(param):
    traduz_texto = 'Não'
    if maior_de_idade:
        traduz_texto = 'Sim'
        return traduz_texto


print(
    f'Nome: {nome}. Idade: {idade}. É maior de idade? {traduz(maior_de_idade)} ')  # noqa

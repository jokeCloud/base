'''
higher order functions
funcoes de primeira classe
'''


def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


saudacao_2 = saudacao

mensgem_1 = saudacao('mensagem de bom dia!', 'alfred')
print(mensgem_1)

print(saudacao_2('oi', 'harold'))


teste = executa(saudacao, 'good day', 'merson')
print(teste)

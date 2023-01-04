'''
closure e funções que retornam outras funções
'''


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar  # closure


bom_dia = criar_saudacao('Bom dia')
boa_tarde = criar_saudacao('Boa tarde')
boa_noite = criar_saudacao('Boa noite')

print(bom_dia('Johanes'))  # closure
print(boa_tarde)
print(boa_noite('Johanes'))  # closure

for nome in ['Maria', 'Joana', 'Luiza']:
    print(bom_dia(nome))
    print(boa_tarde(nome))

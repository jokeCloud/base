pessoa_1 = {}


pessoa_1['nome'] = 'johansen'
sobrenome = 'sobrenome'

pessoa_1[sobrenome] = 'masterson'

print(pessoa_1)
print(pessoa_1['nome'])
print(pessoa_1['sobrenome'])


pessoa_1['nome'] = 'marcos'

print(pessoa_1)
print(pessoa_1['nome'])
print(pessoa_1['sobrenome'])


del pessoa_1['sobrenome']

print(pessoa_1)
print(pessoa_1['nome'])

if pessoa_1.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa_1['sobrenome'])

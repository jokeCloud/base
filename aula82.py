# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'johansen',
    'sobrenome': 'masterson',
    'idade': '900'
}

print(p1['nome'])
print(p1.get('nome', 'Não existe'))


nome = p1.pop('nome')
print(p1, nome)


ultimo_item = p1.popitem()
print(p1, ultimo_item)

p1.update({
    'nome': 'novo_nome',
    'idade': '90',
})
print(p1)

p1.update(mes_nascimento='janeiro')
print(p1)

tupla = ('dia_nascimento', '10'),
p1.update(tupla)
print(p1)

tupla_2 = (('apelido', 'mamao'), ('sobre_apelido', 'mamoa'))
p1.update(tupla_2)
print(p1)

lista = (['dia_da_sorte', 'sexta-feira'], ['mes_de_sorte', 'janeiro'])
p1.update(lista)
print(p1)

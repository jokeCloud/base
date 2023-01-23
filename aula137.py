# __dict__ e vars para atrinutos de instancia
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


joao = Pessoa('johan', 35)

joao.nome = 'joao'
print(joao.nome)
print(joao.__dict__)
print(vars(joao))
del joao.nome
print(joao.idade)
print(joao.__dict__)
print(vars(joao))

joao.__dict__['sobrenome'] = 'masterson'
print(joao.__dict__)
print(vars(joao))

dados = {
    'nome': 'helena',
    'idade': 35
}
helena = Pessoa(**dados)
print(helena.__dict__)

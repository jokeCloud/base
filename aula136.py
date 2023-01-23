class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


joao = Pessoa('johan', 35)
helena = Pessoa('helena', 12)

print(Pessoa.ano_atual)

print(joao.get_ano_nascimento())
print(helena.get_ano_nascimento())

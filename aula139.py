# métodos de classe + factories (fábricas)
# são métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


joao = Pessoa('joao', 43)
print(Pessoa.ano)
Pessoa.metodo_de_classe()

helena = Pessoa.criar_com_50_anos('helena')
print(helena.nome, helena.idade)

anonimo = Pessoa.criar_sem_nome(25)
print(anonimo.nome, anonimo.idade)

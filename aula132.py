# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

string = 'johansen'  # str
print(string.upper())
print(isinstance(string, str))

# class PascalCase  NomeDaClasse ex: CriarBaseDeDados


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


johansen = Pessoa('johansen', 'masterson')
# p1.nome = 'johansen'
# p1.sobrenome = 'masterson'
print(isinstance(johansen, Pessoa))
print(johansen.nome)
print(johansen.sobrenome)

maykelson = Pessoa(nome='maykelson', sobrenome='masterson')
# p2.nome = 'maykelson'
# p2.sobrenome = 'masterson'
print(isinstance(maykelson, Pessoa))
print(maykelson.nome)
print(maykelson.sobrenome)

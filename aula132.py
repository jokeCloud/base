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

string = 'joao'  # str
print(string.upper())
print(isinstance(string, str))

# class PascalCase  NomeDaClasse


class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'johansen'
p1.sobrenome = 'masterson'

p2 = Pessoa()
p2.nome = 'maykelson'
p2.sobrenome = 'masterson'


print(p1.nome)
print(p2.nome)

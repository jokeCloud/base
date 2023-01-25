# exercicio com classes
# 1 - crie uma classe Carro (nome)
# 2 - crie uma classe Motor (nome)
# 3 - crie uma classe Fabricante (nome)
# Obs.: Um motor pode ser de vários carros
# 5 - faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela.


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
v8 = Motor('V8')
volkswagen = Fabricante('Volkswagen')

print(fusca.nome, v8.nome, volkswagen.nome)

brasilia = Carro('Brasilia')
brasilia.motor = 'V3'
print(brasilia.nome, brasilia.motor, brasilia.fabricante)

aventator = Carro('Aventator')
lamborghini = Fabricante('Lamborghini')
motor_lamborghini = Motor('5.3')
aventator.fabricante = lamborghini
aventator.motor = motor_lamborghini

print(aventator.nome, aventator.motor.nome, aventator.fabricante.nome)

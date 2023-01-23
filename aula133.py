# métodos em instâncias de classes python

class Car:
    def __init__(self, marca, modelo, cor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.pneus = 4

    def frear(self):
        print('está agora a 00 km/h')

    def acelerar(self):
        self.aceleracao = input('Pisou "fundo", "mediano" ou "pouco"? ')
        self.aceleracao = self.aceleracao.lower()
        if self.aceleracao == 'fundo':
            print('está agora a 90 km/h')
        elif self.aceleracao == 'mediano':
            print('está agora a 60 km/h')
        elif self.aceleracao == 'pouco':
            print('está agora a 30 km/h')
        else:
            print('tendi não')

    def ligar(self):
        print('vrurruruururururu ta ta ta pa pa')


fusca = Car('volkswagen', 'fusca', 'azul')

fusca.ligar()

brasilia = Car
brasilia.marca = 'volkswagen'
print(f'marca da brasilia é {brasilia.marca}')


fusca.acelerar()
print(f'modelo {fusca.modelo} possui {fusca.pneus} pneus')

carro_de_tres_rodas_mrs_bean = Car

carro_de_tres_rodas_mrs_bean.pneus = 3

print(carro_de_tres_rodas_mrs_bean.pneus)


ka = Car('ford', 'ka', 'preto')

print(ka.modelo, ka.marca, ka.cor)


class Biscoito:
    def __init__(self, sabor):
        self.sabor = sabor

    def diz_sabor(self):
        print(f'tenho o sabor de {self.sabor}')


biscoito_de_chocolate = Biscoito('chocolate')

biscoito_de_creme = Biscoito('creme')

biscoito_de_chocolate.diz_sabor()

biscoito_de_creme.diz_sabor()

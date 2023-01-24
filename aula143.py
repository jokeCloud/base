# @property + @setter - getter e setter no modo python
# como getter
# p/ evitar querbar código cliente
# p/ habilitar setter
# p/ executar ações ao obter um atributo
# atributos que começam com um ou dois __(underlines)
# não devem ser usado fora da classe.

class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        # print('property')
        return self._cor

    @cor.setter
    def cor(self, valor):
        # print('estou no setter', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


def mostrar(caneta):
    return caneta.cor


caneta = Caneta('Azul')
caneta.cor = 'vermelho'
caneta.cor_tampa = 'Azul'

# getter -> obter valor
# mostrar(caneta)
print(caneta.cor)
print(caneta.cor_tampa)

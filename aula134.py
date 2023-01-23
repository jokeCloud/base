# escopo da classe e dos métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def acao(self):
        print(f'{self.nome} está fazendo algo.')

    def dormir(self):
        print(f'{self.nome} está dormindo.')

    def comer(self, alimento):
        print(f'{self.nome} está comendo {alimento}')

    def executar(self, *args, **kwargs):
        return self.comer(*args, **kwargs)


leao_leo = Animal(nome='leozin')

print(leao_leo.nome)

mickey_o_macaco = Animal('Mickey')
print(mickey_o_macaco.nome)

alfred_o_gato = Animal
alfred_o_gato.nome = 'Alfson'

print(alfred_o_gato.nome)


mickey_o_macaco.acao()
leao_leo.dormir()
mickey_o_macaco.comer('banana')
verduras = ['cenoura', 'quiabo', 'nabo']
leao_leo.executar(verduras)

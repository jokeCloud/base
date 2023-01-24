# relações entre classes: associação, agregação e composição
# composição é uma especialização da agregação
# mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são apagadas
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

        def __del__(self):
            print('Apagando,', self.rua, self.numero)


cliente1 = Cliente('maria')
cliente1.inserir_endereco('av brasil', 55)
cliente1.inserir_endereco('av israel', 46)

cliente1.listar_enderecos()
print()

cliente2 = Cliente('joao')
cliente2.inserir_endereco('av brasil', 82)
cliente2.listar_enderecos()

del cliente2

print(cliente1.enderecos[0].rua)
print(cliente1.enderecos[0].numero)
print(cliente1.enderecos[0:(len(cliente1.enderecos))])

print('#####AQUI TERMINA O CÓDIGO')

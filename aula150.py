# class principal (Pessoa)
#   -> super class, parente class, base class
# class filha (Cliente)
#  ->  sub class,   child class,  derived class

class Pessoa:
    """
    Classe Pessoa modelo de criacao de um objeto do tipo Pessoa
    """
    cpf = '23123'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        """
        diz o nome, sobrenome e nome da classe deste objeto que invocou o método
        """
        print(self.nome, self.sobrenome, self.__class__.__name__)


# help(Pessoa)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('estou no método da classe filha e não na classe pai')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    pass


joao_cliente = Cliente('joao', 'pessoa')
print(joao_cliente.nome, joao_cliente.sobrenome)
joao_cliente.falar_nome_classe()


maria_aluna = Aluno('maria', 'nazaré')
print(maria_aluna.nome, maria_aluna.sobrenome)
maria_aluna.falar_nome_classe()

joao_cliente.falar_nome_classe()
# help(Pessoa)

print(joao_cliente.cpf)

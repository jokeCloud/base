# class principal (Pessoa)
#   -> super class, parente class, base class
# class filha (Cliente)
#  ->  sub class,   child class,  derived class

class Pessoa:
    """
    Classe Pessoa modelo de criacao de um objeto do tipo Pessoa
    """

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


help(Pessoa)


class Foo(object):
    pass


help(Foo)

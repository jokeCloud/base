# @staticmethod (métodos estáticos) são inutes em python
# métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls
# em resumo, são funções que existem dentro da classe

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('oi de dentro da classe', args, kwargs)


def funcao(*args, **kwargs):
    print('oi de dentro da funcao', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe()
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)

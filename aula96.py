# dir, hasattr e getattr em python

string = 'joao'
metodo = 'upper'


if hasattr(string, metodo):
    print('este objeto possui o método upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o método', metodo)

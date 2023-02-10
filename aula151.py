class MinhaString(str):
    def upper(self):
        print('Chamou antes do upper na tela')
        retorno = super().upper()
        print('Chamou depois do upper na tela')
        return retorno


string = MinhaString('jon')
print(string.upper())


class A:
    atributo_a = 'valor a'

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def metodo(self):
        super().metodo()
        print('C')


c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

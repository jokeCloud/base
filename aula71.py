'''
escopo de funções em python
escopo significa o local onde aquele código pode atingir
existe o escopo global e local
o escopo global é o escopo onde todo o código é alcançavel
o escopo local é  escopo onde apenas nome do mesmo local
podem ser alcançados
'''
x = 10


def escopo():
    global x
    x = 100

    def outra_funcao():
        global x
        x = 11
        y = 2
        print('outra_funcao(): ', x+1, y+1)

    print('escopo():', x+2)
    outra_funcao()


print(x)
escopo()
print(x)

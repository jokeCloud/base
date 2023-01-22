# problema com parametros mutaveis em funcoes

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('joao')
adiciona_clientes('joana', cliente1)
print(cliente1)
cliente1.append('jao')
print(cliente1)


cliente2 = adiciona_clientes('maria')
adiciona_clientes('helena', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('marcos')
adiciona_clientes('aurelio', cliente3)
print(cliente3)

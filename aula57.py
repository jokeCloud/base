"""
faça uma lista de comprar com listas
o usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lita
não permita que o programa quebre com
erros de indices inexistentes na lista.
"""
import os

itens = []

while True:
    print('Escolha uma opção')
    opcao = input('[I]nserir, [L]istar, [A]pagar: ')

    if opcao:
        opcao = opcao.lower()
        if opcao == 'i':
            item = input('Digite o nome do item: ')
            itens.append(item)
            os.system('clear')
        elif opcao == 'l':
            if len(itens) == 0:
                print('Lista vazia.')
            for chave, valor in enumerate(itens):
                print(chave, valor)
        elif opcao == 'a':
            apagar = input('Digite o indice do item: ')
            apagar = int(apagar)
            del itens[apagar]
            os.system('clear')
    else:
        print('Digite uma opção válida.')

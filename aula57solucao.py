import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir, [l]istar, [a]pagar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digitar um número.')
        except IndexError:
            print('Indice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('por favor, escolha i, a ou l')

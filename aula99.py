# try, except, else e finally

a = 19
b = 0
# c = a / b
linha = [0]
try:
    print(linha[1])
    c = a / b
except ZeroDivisionError:
    print('Divisão por zero')
except NameError:
    print('buscado objeto que não foi definido')
except (TypeError, IndexError) as error:
    print('problema com tipagem dos objetos declarados')
    print('msg:', error)
    print('nome:', error.__class__.__name__)
    print('nome:', NameError(error))
except Exception:
    print('erro desconhecido')

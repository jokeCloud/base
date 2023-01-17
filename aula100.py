# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print('dividiu por zero:', e)
except TypeError as e:
    print('dividiu por zero:', e)
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')

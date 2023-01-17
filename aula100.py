# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as zero:
    print('dividiu por zero:', zero)
finally:
    print('FECHAR ARQUIVO')

# operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avalida naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que é um valor usado para representar um valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Qual é o senha: ')

senha_permitida = 'peixe'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
if senha_digitada == senha_permitida and entrada == 'E' or entrada == 'e':
    print('Pode entrar')
elif entrada == 'S' or entrada == 's':
    print('Até mais')
elif senha_digitada != senha_permitida:
    print('Senha errada.')
else:
    print('Digite "E" para entrar ou "S" para sair, não há outras opções.')


print(True and True and True)
print(True and 1 and True)
print(True and 'a' and True)

# avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
print(True and '' and True)

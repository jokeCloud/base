"""
Faça um programa que peça ao usuário digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
if numero_digitado_pelo_usuario.isdigit():
    numero_tratado_int = int(numero_digitado_pelo_usuario)
    par_impar = numero_tratado_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')


try:
    numero_tratado_int = int(numero_digitado_pelo_usuario)
    par_impar = numero_tratado_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
"""

numero_digitado_pelo_usuario = input('Digite um número inteiro: ')

numero_tratado_int = int(numero_digitado_pelo_usuario)

if numero_tratado_int:
    if numero_tratado_int % 2 == 0:
        print(f'{numero_tratado_int} é par.')
    else:
        print(f'{numero_tratado_int} é ímpar.')
else:
    print('O que você digitou não é um número inteiro.')


"""
Faça um programa que pergutne a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
"""
horario_digitado_pelo_usuário = input('Digite a hora: ')

horario_extraido = horario_digitado_pelo_usuário[0] + \
    horario_digitado_pelo_usuário[1]

horario_tratado = int(horario_extraido)

if horario_tratado >= 6 and horario_tratado <= 11:
    print(f'Bom dia! {horario_tratado}hr')
elif horario_tratado >= 12 and horario_tratado <= 17:
    print(f'Boa tarde! {horario_tratado}hr')
elif horario_tratado >= 18 and horario_tratado <= 23:
    print(f'Boa noite! {horario_tratado}hr')
else:
    print(f'Muito tarde! {horario_tratado}hr')

"""
entrada = input('digite uma hora em números inteiros: )

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor digite apenas números inteiros')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4
letras ou menor escreva 'seu nome é curto' se tiver entre 5 e 6 letras,
escreva 'seu nome é normal'; maior que 6 escreva 'seu nome é muito grande'
"""
nome_do_usuario = input('Digite seu primeiro nome: ')

if nome_do_usuario:
    if len(nome_do_usuario) <= 4:
        print('Seu nome é curto.')
    elif len(nome_do_usuario) == 5 or len(nome_do_usuario) == 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Por favor, digite seu nome.')

"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome >= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 or tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Por favor, não envie o campo sem preencher')
"""

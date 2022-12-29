"""
faça um jogo para o usuário adivinhar qual a palavra secreta.

você vai propor uma palavra secreta qualquer e vai dar
 a possibilidade para o usuário digitar apenas uma letra.

qual o usuário digitar uma letra, você vai conferir se a
digitada está na palavra secreta
    se a letra digitada estiver na palavra secreta;
    exiba a letra;

    se a letra digitar não estiver na palavra secreta;
    exiba *. faça a contagem de tentativas do seu usuário
"""

palavra_secreta_facil = 'peixe'
palavra_secreta_dificil = 'alfandegueiros'
palavra_secreta_muito_dificil = 'oftalmotorrinolaringologista'


palavra_secreta = ''

print('\n')
print('Jogo "Descubra a palavra secreta". \n')
nivel = input(
    'Quer jogar em qual nível? [1]Fácil, [2]Difícil, [3]Muito Difícil: ')

limite = 0

if nivel == '1':
    palavra_secreta = palavra_secreta_facil
    limite = 10
elif nivel == '2':
    palavra_secreta = palavra_secreta_dificil
    limite = 20
elif nivel == '3':
    palavra_secreta = palavra_secreta_muito_dificil
    limite = 40
else:
    palavra_secreta = palavra_secreta_facil
    limite = 10

print('\n')
print('Digite uma letra para ver se contém na palavra. Você tem 10 chances. \n')  # noqa


palavra_secreta_encontrada = ''
erros = ''

for i in range(limite):
    letra_do_usuario = input('Escolha uma letra: ')
    if len(letra_do_usuario) > 1:
        print('Digite apenas uma letra. \n')
        continue
    letra_do_usuario = letra_do_usuario.lower()

    if letra_do_usuario in palavra_secreta:
        contador = palavra_secreta.count(letra_do_usuario)
        print('\n')
        print(f'"{letra_do_usuario}" foi uma boa escolha.')
        palavra_secreta_encontrada += contador * letra_do_usuario
    else:
        erros += '*'
        print('Escolha ruim.')
    if erros:
        print(f'quantidade de erros: {len(erros)} \n')
    if len(palavra_secreta_encontrada) == len(palavra_secreta):
        print('\n')
        print(f'Você ganhou! Palavra secreta era: {palavra_secreta} \n')
        break

print('Você perdeu!')

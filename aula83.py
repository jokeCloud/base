# exercicios - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


print(f'Jogo de perguntas: serão {len(perguntas)} perguntas.')

contador_de_erros = 0

for pergunta in perguntas:
    for chave, valor in pergunta.items():
        if chave == 'Pergunta':
            print(f'\n{chave}: {valor}\n')
        if chave == 'Opções':
            print(f'{chave}:')
            for indice, opcao in enumerate(valor):
                print(f'{indice}) {opcao}')
        if chave == 'Resposta':
            escolha_do_usuario = input('Escolha uma opção: ')
            escolha_do_usuario_tratado = int(escolha_do_usuario)
            if pergunta['Opções'][escolha_do_usuario_tratado] == valor:
                print('👍')
            else:
                print('👎')
                contador_de_erros += 1

print(
    f'\nVocê acertou: {len(perguntas)-contador_de_erros} de {len(perguntas)} perguntas.\n')  # noqa

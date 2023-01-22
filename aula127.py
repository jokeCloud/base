# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

tarefas = []
ultima = ''
temporaria = ''
comando = ''


while True:
    print('Comandos: listar, desfazer, refazer, sair')
    entrada = str(input('Digite uma tarefa ou comando: '))
    print()

    if entrada == 'listar' or entrada == 'desfazer' or entrada == 'refazer' or entrada == 'sair':  # noqa
        comando = entrada.lower()
    else:
        entrada = entrada.lower()
        tarefas.append(entrada)
        temporaria = entrada

    if comando == 'listar':
        for tarefa in tarefas:
            print(tarefa)
        print()

    if comando == 'desfazer':
        temporaria = tarefas.pop()
        for tarefa in tarefas:
            print(tarefa)
        print()

    if comando == 'refazer':
        tarefas.append(temporaria)
        for tarefa in tarefas:
            print(tarefa)
        print()

    if comando == 'sair':
        break

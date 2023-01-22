import os


def listar(tarefas):
    print()
    if not tarefas:
        print('nenhuma tarefa para listar')
        return

    print('tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('você não digitou nenhuma tarefa')
        return
    tarefas.append(tarefa)


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        continue

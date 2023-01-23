import json

from aula138 import CAMINHO_DO_ARQUIVO, Pessoa

with open(CAMINHO_DO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)

    joao = Pessoa(**pessoas[0])
    marcos = Pessoa(**pessoas[1])
    maria = Pessoa(**pessoas[2])

    print(joao.nome, joao.sobrenome)
    print(marcos.nome, joao.sobrenome)
    print(maria.nome, maria.sobrenome)

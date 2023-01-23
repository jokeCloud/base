# exercicio - salve sua classe em json
# salve os dados da sua classe em json
# e depois crie novamente as instancias
# da classe com os dados salvos
# faca em arquivos separados

import json

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
}
arquivo_json = json.dumps(dicionario)

print(dicionario)
print(arquivo_json)

'''
ler
crair a classe
salvar os dados
salvar esses dados
criar outro arquivo
recuperar esses dados
e recriar as classes
'''

CAMINHO_DO_ARQUIVO = 'aula138.json'


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


joao = Pessoa('johansen', 'masterson')
marcos = Pessoa('marcos', 'masterson')
maria = Pessoa('maria', 'masterson')
bd = [vars(joao), marcos.__dict__, vars(maria)]


def fazer_dump():
    with open(CAMINHO_DO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    fazer_dump()

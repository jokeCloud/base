# decorators
# decorar = adicionar / remover / restringir / alterar
# funcoes que decoram outras funcoes
# decoradores são usados para fazer o python
# usar as funcoes decoradores em outras funcoes
# decoradores são syntax sugar (sintaxe doce) ou (melzinho na chupeta) sintaxe mais simples

# def inverte_string(string):
#     return string[::-1]


# def diz(phrase):
#     return phrase


# print(inverte_string(diz('ola')))

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        resultado += 'lan'
        print(f'o seu resultado foi: {resultado}')
        print('ok, decorado')
        return resultado
    return interna


@criar_funcao  # syntax sugar - more simple - little honey
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


# sem syntax sugar
inverte_string_chechando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_chechando_parametro('123')
print(invertida)

# com syntax sugar
inverte_var = inverte_string('123456789')
print(inverte_var)

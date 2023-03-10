# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
try:
    import sys
except ModuleNotFoundError as error_module:
    print('Não foi possível importar modulo:', error_module)

import aula103_m

# from aula103_m import diz_oi, variavel_do_modulo

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')

multiplicador = 3

if __name__ == '__main__':
    aula103_m.diz_oi('oi ' * 10)
    print(aula103_m.variavel_do_modulo)
    print(aula103_m.soma(10, 20))
    print(aula103_m.soma(10, 20) * multiplicador)

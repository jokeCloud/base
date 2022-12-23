# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo
print(11)
print(-11)
print(0)
print(10_000_000_000_000_000)  # underline melhora a leitura

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante
# float sem sinal é considerado positivo.
print(1.1, 10.11, 1_000_000_000.10)


# A função type mostra o tipo que o Python
# inferiu ao valor

variavel_parametro = 'Olá,'


def funcao_diz_oi(param):
    return f'{param} digo oi.'


print(funcao_diz_oi(variavel_parametro))

# ANOTAÇÃO IMPORTANTE, tudo em python é um objeto

print(type('string.texto.str'), 'string.texto.str')
print(type(0), 0)
print(type(1.1), 1.1)
print(type(0), type(-1), type(1.1), type('texto'))

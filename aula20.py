primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor_convertido = float(primeiro_valor)
segundo_valor_convertido = float(segundo_valor)

if primeiro_valor_convertido > segundo_valor_convertido:
    print(
            f'{primeiro_valor_convertido=:.2f} é maior do que o {segundo_valor_convertido=:.2f}'  # noqa
        )
elif segundo_valor_convertido > primeiro_valor_convertido:
    print(
            f'{segundo_valor_convertido=:.2f} é maior do que o {primeiro_valor_convertido=:.2f}'  # noqa
        )
elif segundo_valor_convertido == primeiro_valor_convertido:
    print(
            f'{segundo_valor_convertido=:.2f} são iguais {primeiro_valor_convertido=:.2f}'  # noqa
        )
else:
    print('Valores digitados não correspondem a números.')

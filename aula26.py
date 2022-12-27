"""
formatação básica de strings
s - string
d - int(decimal)
f - float
.<número de digitos>f
x ou X - Hexadecimal minúsculo ou maísculo
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - força o sinal a esquerda
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4873648123746:.1f}')
print(f'{1000.4873648123746:,.1f}')
print(f'{1000.4873648123746:+,.1f}')
print(f'{-1000.4873648123746:+,.1f}')
print(f'{-1000.4873648123746:0>+,.1f}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
print(f'{variavel!s}')
print(f'{variavel!a}')

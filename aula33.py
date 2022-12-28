"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool -> são objetos
"""
string = 'Johansen Masterson'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC'
# print(string)
print(outra_variavel)
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.join('ov'))
print(string.zfill(10))

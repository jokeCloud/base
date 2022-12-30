"""
impecisão de ponto flutuante
double-precision floating-point format IEEE 754
"""

import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
numero_4 = decimal.Decimal(0.1)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5

print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3))
print(round(numero_3, 1))
print(round(numero_3, 2))
print(round(numero_3, 3))

print(numero_6)
print(f'{numero_6:.2f}')
print(round(numero_6))
print(round(numero_6, 1))
print(round(numero_6, 2))
print(round(numero_6, 3))

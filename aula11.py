# 1. (n + n)        parentesis
# 2. **             exponenciacao
# 3. * / // %       multiplicação, divisão e módulo
# 4. + -            adição e subtração

conta_1 = 1 + 1 ** 5 + 5      # 1024 tentativa
conta_2 = (1 + 1) ** (5 + 5)  # 1024
conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)  # 1024

print(conta_1)
print(conta_2)
print(conta_3)

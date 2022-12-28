# while

contador = 0

while contador <= 100:
    contador += 1

    if contador % 6 == 0:
        print('não mostrar divisiveis por 6')
        continue

    if contador % 8 == 0:
        print('não mostrar divisiveis por 8')
        continue

    if contador == 50:
        break

    print(contador)


print('Acabou')

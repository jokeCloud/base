import importlib

import aula104_m

print(aula104_m.variavel_1)

for i in range(10):
    importlib.reload(aula104_m)
    print(i)


print('fuim')

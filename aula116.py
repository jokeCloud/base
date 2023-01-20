# count é um iterador sem fim
from itertools import count

c1 = count(step=2, start=2)
r1 = range(4, 10, 2)

print(r1)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i > 10:
        break

    print(i)

print()

print('range')
for i in r1:
    if i > 10:
        break

    print(i)

import sys

# generator expression, iterables e iterators em python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # iterable.__iter__()   tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) StopIteration

lista = [n for n in range(10)]
generator = (n for n in range(10))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)

import sys

#Generator expression, iterables e iterators em python

iterable = ["Eu", 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem __iter__ e __next__
lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print(generator)
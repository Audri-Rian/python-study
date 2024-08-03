# Generator expression, Iterables e iterators em Python

iterable = ["Eu", 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem __iter__ e __next__

print(next(iterator)) # O iterator sabe APENAS o próximo valor
print(next(iterator))
print(next(iterator))
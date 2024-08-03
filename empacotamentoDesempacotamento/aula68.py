#isinstace - para saber se o objeto é determinado tipo
lista = [
    'a', 1 ,1.1 , True, [0,1,2], (1,2),
    {0,1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, set):
        item.upper
        print(item, isinstance(item, set))
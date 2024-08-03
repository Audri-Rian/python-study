# Função lambda em python
# A função lambda é uma função como qualquer outra me Python.
# Porém, são funções anônimas que contem apenas uma linha.
# Ou seja, tudo deve ser contido dentro de uma única expressão
lista = [
    {'nome': 'Audri', 'Sobrenome': 'miranda'}, 
    {'nome': 'Carlos', 'Sobrenome': 'miranda'}, 
    {'nome': 'Queiroz', 'Sobrenome': 'miranda'}, 
    {'nome': 'PEdrfo', 'Sobrenome': 'miranda'}, 
    {'nome': 'Orinittorinco', 'Sobrenome': 'miranda'}, 
]

# def orderna(item):      #A função lambda faz a mesma coisa que essa função aqui so que em uma unica linha
#     return item ['nome']

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['Sobrenome'])

exibir(l1)
exibir(l2)

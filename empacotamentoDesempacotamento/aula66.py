# List comprehension em Python
# List comprehension é uma forma rapída para criar listas a partir de iteráveis

lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]

print(list(range(10)))
print(lista)

#Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco' : 20, },
    {'nome': 'p2', 'preco' : 10, },
    {'nome': 'p3', 'preco' : 30, },
]

novos_produtos =[
    {'nome': produto['nome'], 'preco': produto['preco']}
    for produto in produtos
]

print(*novos_produtos, sep='\n')
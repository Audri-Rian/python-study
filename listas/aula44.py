'''
# Enumarate - Enumera iteráveis (índices)
'''

listas = ['Maria', 'Helena', 'Luiz']
listas.append('João')

listas_enumerada = enumerate(listas) #Enumera a lista

for item in listas_enumerada:
    print(item)
'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'Olha so qué, coisa atraente'
lista_palavras = frase.split(',') # Divide a partir da ,

lista_palavras_fixed=lista_palavras
for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()

print(lista_palavras)
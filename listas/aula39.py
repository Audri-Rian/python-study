'''
Lista é uma função mutável
É um dado mutável

Append - Adiciona um item ao final da lista
Insert - Adiciona um item no índice escolhido
pop - Remove do final ou do índice escolhido
del - Apaga um índice
clear - limpa a lista
extend - Estende a lista
+ - Concatena listas
'''
lista1 = [10,20,30,40]
lista1[2]= 300
del lista1 [2] # Deleta o indice de acordo com a lista
lista1.append('Cupreto') # Adiciona apenas no final
lista1.pop() #Adicionei o CuPreto a lista, mas com esse comando eu removi ele da lista
lista1.append(12)
lista1.insert (0,3) #Adicionei o número 3 a lista no indice 0
print(lista1)

lista2 = [0,7,4]

lista3 = lista1 +lista2
print(lista3)


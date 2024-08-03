#Sets - conjuntos em python (tipo set)
#COnjuntos ensinados na matemática
#Representados graficamente pelo diagrama de Venn
#Sets são mutáveis, porém aceitam apenas tipos imutáveis com o valor interno.

#Criando um set

s1 = set('Luiz') #ou s1 = {'Luiz'}
print(s1)

#Sets são eficientes para remover valores duplicados de iteráveis 
#Seus valores serão sempre únicos
#Não aceitam valores mutáveis 
#Não tem índexes
#Não garantem ordem
#São iteráveis (for, in, not in)

l1 =[1,2,3,3,4,4,5,5,5]
s2 = set(l1)
print(s2)
print(4 in s2) 
s1 = set()
s1.add('Audri')
s1.add(1)
s1.update(('Olá mundo',1,2,3,4))
#s1.clear() Dar clear
s1.discard('Olá mundo')
print(s1)

s1 ={1,2,3}
s2 ={2,3,4}
s3 = s1 | s2 #União - Une as 2 listas
s4 = s1 & s2 #Intersecção - Itens presentes em ambos
s5 = s1 - s2 #Diferença - Itens presentes apenas no set da esquerda
s6 = s1 ^ s2 #Diferença simétrica ^ - Itens que estão presente em ambos
print(s3)
print(s4)
print(s5)
print(s6)
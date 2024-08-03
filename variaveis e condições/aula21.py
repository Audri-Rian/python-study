'''
interpolação basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal(ABDCEF0123456789)
'''

nome = "Audri"
preco = 1000.44440
variavel = '%s, o preço é R$%.2f' %(nome,preco)
print(variavel)
print("O hexadecimal de %d é %08x" % (1500,1500))
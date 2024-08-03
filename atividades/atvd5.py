#       0123456789
nome = "Audri Rian" #Iteráveis
#       0123456789

tamanho_nome = len(nome)

i = 0
novo_nome = ''
while i <len(nome):
    letra = nome[i]
    novo_nome += letra
    i += 1

print(novo_nome)
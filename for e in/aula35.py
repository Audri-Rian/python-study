texto = "Audri"


novo_texto = ''
for letra in texto: # para cada letra em interavel(texto) exiba a letra
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
'''
Iteravel -> Str,range, etc (___iter___)
iterador -> QUem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

texto = "Audri" #iterável
iteratador = iter(texto) #iterator

while True: #essa viadagem aqui é a explicação de como funciona o for e IN
    try:
        letra = next(iteratador)
        print(letra)

    except StopIteration:
        break

for letra in texto: #Essa pora aqui é igual ao while ali am cima
    print(letra)
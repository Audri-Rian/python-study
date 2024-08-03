try:
    nome = input("Digite seu nome: ")
    nome = len(nome)
    nome_curto = nome <=4
    nome_normal = nome >= 5 and nome <= 6
    nome_grande = nome > 6 

    if nome_curto:
        print("Seu nome é curto")
    if nome_normal:
        print("Seu nome é normal")
    if nome_grande:
        print("Seu nome é muito grande")

except:
    print("Você não digitou um nome")
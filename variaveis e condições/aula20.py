nome = input('digite seu nome: ')
encontrar = input("digite o que deseja encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em nome {nome}')
else:
    print(f'{encontrar} não está em {nome}')
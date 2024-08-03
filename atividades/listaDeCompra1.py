compras =[]

while True:
    print("Escolha umas das opções abaixo: ")
    print("1- Adicionar um item a lista ")
    print("2- Remover da lista: ")
    print("3- Listar valores da sua lista")
    opcoes = (int(input("Escolha: ")))

    if opcoes == 1:
        item = input("Adicione uma compra ao seu carrinho: ")
        compras.append(item)
    
    if opcoes == 2:
        if compras ==0:
            print("Você ainda não adicionou nenhum item ao carrinho")
        else:
            item = input("Digite o item que deseja remover: ")
            if item in compras:
                compras.remove(item)
                print(f'{item} foi removido da lista.')
            else:
                print('O item não está na lista') 

    if opcoes == 3:
        print(compras)
peso = input("Qual foi o peso: ")
peso = int(peso)
peso_excedente = peso - 50


if peso >50:
    print('Você foi multado')
    print(f'Você ultrapassou o peso máximo permitido em {peso_excedente} quilos')
    print(f'Então você tera que pagar em multa R${peso_excedente * 4}')

else:
    print("Você não foi multado")
    
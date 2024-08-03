ano = int(input("Digite qualquer ano: "))

if (ano % 4 == 0 and ano %100 !=0) and (ano%400==0):
    print(f'O {ano} é bissexto!')
else:
    print(f'O {ano} não é bissexto!')


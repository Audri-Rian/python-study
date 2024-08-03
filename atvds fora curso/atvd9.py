num1 =input('Digite um numero inteiro: ')
num2 = input('Digite outro numero inteiro: ')
num3 = input("Agora digite um numero fracionario: ")

num1 = int(num1)
num2 = int(num2)
num3 = float(num3)

print(f'O produto do dobro do primeiro com a metade do segundo: {(num1*2)*(num2/2)}')
print(f'A soma do triplo do primeiro com o terceiro: {num3+(num1*3)}')
print(f'O teceiro elevado ao cubo {num3**3}')
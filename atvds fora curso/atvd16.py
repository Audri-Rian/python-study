num = input("Digite um numero inteiro: ")
num = int(num)

resultado = num%2
print(resultado)
if resultado == 0:
    print(f"O {num} é par")
else:
    print(f"O {num} é impar")
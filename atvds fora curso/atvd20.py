num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

if num1 >= num2 and num1 >=num3:
    maior = num1
elif num2 >= num1 and num2 >=num3:
    maior =num2
else:
    maior = num3

if num1 <= num2 and num1 <=num3:
    menor = num1
elif num2 <= num1 and num2 <=num3:
    menor =num2
else:
    menor = num3

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')
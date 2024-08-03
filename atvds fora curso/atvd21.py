num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

maior = max(num1,num2,num3)
menor = min(num1,num2,num3)

meio = (num1 +num2 +num3) - maior - menor

print(f"Em ordem decrescente {maior}, {meio}, {menor}")
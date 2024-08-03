#Eu deveria usar o comando .isdigit para reconhecer se o numero é inteiro

try:
    num = int(input("Digite um número: "))
    impar_par = num % 2
    
    if impar_par == 0:
        print("O seu numero é positivo")
    else:
        print("O seu numero é impar")

except:
    print("Você não digitou um numero inteiro")
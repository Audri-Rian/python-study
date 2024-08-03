salario = float(input("Qual o seu salário? "))

if salario <=280:
    aumento = (salario*20)/100
    print(f"Seu salario antes do reajuste R${salario}")
    print(f"O aumento será de 20%")
    print(f"O valor do aumento é R${aumento}")
    print(f'O seu novo salário, após o aumento é R${aumento+salario}')
elif salario >280 and salario <=700:
    aumento = (salario*15)/100
    print(f"Seu salario antes do reajuste R${salario}")
    print(f"O aumento será de 15%")
    print(f"O valor do aumento é R${aumento}")
    print(f'O seu novo salário, após o aumento é R${aumento+salario}')
elif salario >700 and salario <=1500:
    aumento = (salario*15)/100
    print(f"Seu salario antes do reajuste R${salario}")
    print(f"O aumento será de 15%")
    print(f"O valor do aumento é R${aumento}")
    print(f'O seu novo salário, após o aumento é R${aumento+salario}')
else:
    aumento = (salario*5)/100
    print(f"Seu salario antes do reajuste R${salario}")
    print(f"O aumento será de 5%")
    print(f"O valor do aumento é R${aumento}")
    print(f'O seu novo salário, após o aumento é R${aumento+salario}')
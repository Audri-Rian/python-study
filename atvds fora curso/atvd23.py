hora = int(input("Quantas horas trabalhadas no mês? "))
valor_hora = float(input("Qual o valor da sua hora? "))

salario_bruto = hora*valor_hora

inss = (salario_bruto*10)/100
fgts = (salario_bruto*11)/100
sindicato =(salario_bruto*3)/100
IR = 0
total_descontos = inss + fgts +sindicato + IR

if salario_bruto <=900:
    IR = 0
if salario_bruto >900 and salario_bruto <=1500:
    IR= (salario_bruto *5)/100
if salario_bruto >1500 and salario_bruto <=2500:
    IR= (salario_bruto *10)/100
else:
    R= (salario_bruto *20)/100

print(f'Seu salario bruto é: {salario_bruto}')
print(f'Valor do imposto de renda: R${IR}')
print(f'Valor o INSS R${inss}')
print(f'Valor do FGTS R$ {fgts}')
print(f'Valor do sindicato R${sindicato}')
print(f'Total dos descontos: R${total_descontos}')
print(f'Salario Liquido: {salario_bruto - total_descontos}')
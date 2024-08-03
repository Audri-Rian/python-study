hora = input("Quantas horas você trabalhou no mês? ")
valor_hora = input("Qual o valor da sua hora? ")

hora = int(hora)
valor_hora =float(valor_hora)

valor_bruto = hora*valor_hora
ir = (valor_bruto*11)/100
inss = (valor_bruto*8)/100
sindicato = (valor_bruto*5)/100

print(f'Seu salario bruto: R${valor_bruto}')
print(f'Valor descontado do imposto de renda R${ir}')
print(f'valor descontado do INSS R${inss}')
print(f'Valor descontado do sindicato R${sindicato}')
print(f'Seu salario liquido é R${valor_bruto-ir-inss-sindicato}')
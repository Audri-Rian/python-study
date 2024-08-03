hora = input('Quantas horas você trabalha por mês? ')
valor_hora = input("Qual o valor da sua hora? ")

hora = float(hora)
valor_hora = float(valor_hora)

salario = hora*valor_hora

print(f'O total do seu sario no mês é R${salario}')
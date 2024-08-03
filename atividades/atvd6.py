#Calculadora 
while True:

    num1 = input("Digite um numéro: ")
    num2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None
    num1_float= float(num1)
    num2_float = float(num2)
    try:
        num1_float= float(num1)
        num2_float = float(num2)

        numeros_validos = True
    except Exception:    
        numeros_validos = None

    if numeros_validos is None:
        print("Um dos números são inválidos")
        continue

    operadores_permitidos ='x-/*'

    if operador not in operadores_permitidos:
        print("operador inválidado.")
    
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("Realizando a sua conta. Confira o resultado abaixo: \n")
    if operador =='+':
        print(num1_float + num2_float)
    elif operador =='-':
        print(num1_float - num2_float)
    elif operador =='/':
        print(num1_float / num2_float)
    elif operador =='*':
        print(num1_float * num2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    
    if sair is True:
        print("Você saiu")
        break
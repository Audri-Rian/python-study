lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("DIgite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

equilatero = lado1 == lado2 == lado3
isoceles = lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 !=lado2


while lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado3 +lado1>lado2:
    if equilatero is True:
        print('É um triangulo equilatero')
        break
    elif isoceles is True:
        print("O triangulo é isoceles")
        break
    else:
        print("Triangulo Escaleno")
        break
else:
    print("Não é um triangulo")
    
    
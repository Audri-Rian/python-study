nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota"))

media = (nota1+nota2)/2

if media >9:
    print("Você tirou A")
    aprovado = True

elif media >=7.5 and media <=9:
    print("Você tirou B")
    aprovado = True

elif media >=6 and media <7.5:
    aprovado = True
    print("Você tirou C")

elif media >=4 and media <6:
    print("Você tirou D")
    aprovado = False

else:
    print("Você tirou abaixo de 4, sua nota foi E")
    aprovado = False

while aprovado is True:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado")
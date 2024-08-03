nota1 = input("Digite a primeira nota: ")
nota2 = input("DIgite a segunda nota: ")
nota1 = float(nota1)
nota2 = float(nota2)

media = (nota1+nota2)/2

if media >= 7 and media <=9:
    print(f'Você foi aprovado com {media}')
elif media == 10:
    print(f'Aprovado com distinção com {media}')
else:
    print(f"Você foi reprovado {media}")
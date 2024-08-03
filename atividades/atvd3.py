try:
    hora = float(input("Que horas são: "))
    manha = hora <= 11 and hora >= 0
    tarde = hora >= 12 and hora <= 17
    noite = hora >= 18 and hora <= 23

    if manha:
        print(f"Bom dia são {hora:.2f} da manhã")
    elif tarde:
        print(f"Boa tarde são {hora:.2f} da tarde")
    elif noite:
        print(f"Boa noite são {hora:.2f} da noite")
    else:
        print("Não conheço essa hora")
except:
    print("Você não digitou a hora da maneira correta")
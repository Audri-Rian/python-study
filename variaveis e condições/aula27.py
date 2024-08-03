'''
Isso é pra comprovar a logica de quando passar no if e fazer o entendimento do codigo mais legivel
none = não falor = false
is e is not = é ou não(tipo,valor, Id)
id= identidade
'''
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")

else:
    print("Não faça algo")

if passou_no_if is None:
    print("Não passou no if")

if passou_no_if is True:
    print("Ele passou no")
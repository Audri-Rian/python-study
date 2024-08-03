# Try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    8/0

except ZeroDivisionError:
    print("Dividiu por zero")

else: # O else so vai ser executado quando o codigo foi executado com sucesso
    print('Executado com sucesso')

finally: # O finally vai ser executado mesmo depois do error
    print('FECHAR ARQUIVO')
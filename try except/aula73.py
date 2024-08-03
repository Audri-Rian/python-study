# Try, except, else e finally
#a = 18
#b = 0
#c = a / b

try:
    a = 18
    b = 0
    print('Linha 1')
    c = a / b #Ele pula a partir do momento q acontece o erro para o except
    print('Linha 2')
    
except ZeroDivisionError: #esse ZeroDivision é uma classe
    print("Dividiu por zero.")
except NameError: 
    print("Alguma váriavel não foi definida.")   
except (TypeError , IndexError) as error:
    print("TypeError + IndexError")
    print('MSG: ',error) 
    print('Nome: ',error.__class__.__name__)
except Exception: # Trata qualquer tipo de erro que não foi tratada diretamente
    print('ERRO DESCONHECIDO')
print('Continuar')
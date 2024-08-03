'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é 
'''

x= 1 #Escopo modular(Escopo maior de todos, que é o escopo do arquivo).

def escopo():# Escopo padrão.
    global x #Difinir que o x dessa função(escopo) é global.
    x=10

    def outra_funcao(): # Escopo menor.
        x= 11
        y = 2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x) 

#Todos eles podem atribuir valores diferentes no X ja que cada escopo é diferente.
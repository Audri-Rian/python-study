'''
Escopo de funções em Python
Escopo significa o local onde auqele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma do escopo interno.
'''

x= 1 

def escopo():
    global x 
    x=10

    def outra_funcao(): 
        x= 11 # Se caso esse X não existisse o X dessa função seria o X mais proximo que seria o X da função anterior (10)
        y = 2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x) 


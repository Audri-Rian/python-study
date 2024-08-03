def executa (funcao, *args): # Função de executar
    return funcao(*args)

def soma (x,y): #Posso fazer essa mesma merda com a função lambda em uma unica linha
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return  numero * multiplicador
    return multiplica

# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n*m,
    2
)
print(duplica(2))

print(

    executa(
        lambda x, y: x + y, 2, 3 #A função lambda n tem return
    ),
    executa(soma, 2,3),
    soma(2,3)

)

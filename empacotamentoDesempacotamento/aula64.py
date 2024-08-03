# Empacotamento e desempacotamento de dicionários

pessoa = {
    'nome': 'Audri',
    'sobrenome' : 'Rian',
}

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.6,
}

pessoa_completa = {**pessoa,**dados_pessoa}

print(pessoa_completa)

# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args,**kwargs):

    print('NÃO NOMEADOS: ',  args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome ='Audrinho', qlq=123)
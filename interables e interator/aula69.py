# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False Range (0,10)

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)
 
def falsy (valor):
    return 'fasly' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'')
'''
CLosure e funções que retornam outras funções
'''

def criar_saudacao(saudacao): #Criou uma função que cria OUTRA função
    def saudar(nome):
        return f'{saudacao},{nome}!'
                    # Return sem nada é igual a none
    return saudar() # Sem parentese retorna apenas a função e não o corpo do escopo
    
falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Bom noite")

for nome in ['Audri','Rian','Cordeiro']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
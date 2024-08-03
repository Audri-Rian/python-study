#Dicionarios em Python (tipo Dict)
#Dicionarios são estruturas de dados do tipo par de "Chave" e "valor"
#Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser tipos imutáveis
#como: str, int, float ,bool, tuple, etc.
#O valor pode ser de qualquer tipo, incluindo outro dicionário
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
#Mutável : dict, list

pessoa ={ #Essa pora é um dicionario
    'nome': 'Audri Rian',
    'sobrenome' : 'Cordeiro',
    'idade' : 19,
    'altura' : 1.82,
    'endereços': [
        {'rua': '17 de agosto', 'numero': 42},
        {'rua': 'agosto17 de ', 'numero': 42},
    ],
}

#pessoa = dict(nome='Audri Rian', sobrenome='Codeiro') essa pora é a mesma merda dali de cima

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave,pessoa[chave])
import copy

from dados_tvd import produtos # Aqui estou importando de outra pasta a minha lista especifica de produtos 

novos_produtos = [
    {**p, 'preco':round( p['preco'] * 1.1, 2)}

    for p in copy.deepcopy(produtos) # Estou dando deepcopy dos meus Protudos para os novos produtos
]

produtos_ordernado_por_nome = sorted(
    copy.deepcopy(produtos),
    key= lambda p : p['nome'],
    reverse = True
)

produtos_ordernado_por_preco = sorted(
    copy.deepcopy(produtos),
    key= lambda p : p['preco']
)

print(*produtos, sep='\n')
print()
print(*produtos_ordernado_por_preco, sep='\n')
print()
print(*produtos_ordernado_por_nome, sep='\n')
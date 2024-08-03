#len - Quantas chaves
#Keys - iteravel com chaves
#values - Iteravel com os valores
#Items - iterável com chaves e valores
#setdefault - adiciona valor se a chave não existe
#copy - retorna uma cópia rasa (shallow copy)
#get -Obtém uma chave 
#pop - apaga um item com a chave especificada (del)
#popitem - apaga o último item adicionado 
#update - Atualiza um dicionario com outro

pessoa ={
    'nome' : 'Audri Rian',
    'sobrenome' : 'Cordeiro',
}

print(len(pessoa)) #está lendo a quantidade de chaves dentro do dicíonario
print(pessoa.keys()) #Retorna as chaves
print(list(pessoa.values())) #Retornando apenas os valores
print(list(pessoa.items())) # Retorna a chave e o valor
pessoa.setdefault('idade', 19) #Adicionando ao dicionario
print(pessoa['idade']) 
print(pessoa.get('nome')) #Retorna alguma chave presente, ou não presente

#nome = pessoa.pop('nome') #Remove o item desejado
nome = pessoa.popitem() #Elimina a ultima chave #PILA
print(nome)
print(pessoa)
pessoa.update({ #Atualizando a lista
    "nome" : 'Carlinhos',
    'endereço' : 'Rua 17 de agosto'
})
lista_a = ["Audri RIan",'Maria',1,True,1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Trocado'
print(lista_b) # O comando copy copiou a lista A antes que fosse alterada para "Trocado"
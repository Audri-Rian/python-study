vetor = []

for i in range(10):
    caractere = input(f"Digite o caractere {i+1}: ")
    vetor.append(caractere[0])

vogais = 'aeiouAEIOU'

consoantes = []
contador_consoantes = 0

for caractere in vetor:
    if caractere.isalpha() and caractere not in vogais:
        consoantes.append(caractere)
        contador_consoantes += 1

print(f"Quantidade de consoantes lidas: {contador_consoantes}")
print("Consoantes lidas:", consoantes)
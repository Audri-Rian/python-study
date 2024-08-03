medias_alunos = []


for aluno in range(1, 11):
    notas = []
    print(f"Aluno {aluno}:")
    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias_alunos.append(media)
    print(f"Média do aluno {aluno}: {media:.2f}")


alunos_acima_da_media = 0
for media in medias_alunos:
    if media >= 7.0:
        alunos_acima_da_media += 1

print(f"Número de alunos com média maior ou igual a 7.0: {alunos_acima_da_media}")
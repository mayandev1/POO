qtd_alunos = int(input("Quantos alunos serão cadastrados? "))

soma_medias = 0
aprovados = 0
reprovados = 0

maior_media = -1
melhor_aluno = ""

for i in range(qtd_alunos):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")

    soma_notas = 0

    for j in range(3):
        while True:
            nota = float(input(f"Nota {j+1}: "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota inválida!")

        soma_notas += nota

    media = soma_notas / 3
    soma_medias += media

    print(f"Média: {media:.2f}")

    if media >= 7:
        print("APROVADO")
        aprovados += 1
    elif media >= 4:
        print("RECUPERAÇÃO")
    else:
        print("REPROVADO")
        reprovados += 1

    if media > maior_media:
        maior_media = media
        melhor_aluno = nome

media_geral = soma_medias / qtd_alunos

print("\nRESULTADOS FINAIS:")
print(f"Média geral da turma: {media_geral:.2f}")
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)
print("Melhor aluno:", melhor_aluno)
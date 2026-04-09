qtd_pessoas = int(input("Quantas pessoas serão cadastradas? "))

menores = 0
adultos = 0
idosos = 0
soma_idades = 0

for i in range(qtd_pessoas):
    while True:
        idade = int(input(f"Idade da pessoa {i+1}: "))
        if 0 <= idade <= 110:
            break
        else:
            print("Idade inválida! Digite novamente.")

    soma_idades += idade

    if idade < 18:
        menores += 1
    elif idade <= 59:
        adultos += 1
    else:
        idosos += 1

media = soma_idades / qtd_pessoas

print("\nRESULTADOS:")
print("Menores de idade:", menores)
print("Adultos:", adultos)
print("Idosos:", idosos)
print("Média das idades:", media)
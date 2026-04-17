lista__de_temperaturas = []
soma = 0
media = 0

print("Digite as temperaturas (valor negativo para parar):")

while True:
    num = float(input())

    if num < 0:
        media = soma/tamanho
        print(f"\nMedia das temperaturas registradas: {media}")
        print("Temperaturas:")
        print(lista__de_temperaturas)
        break

    lista__de_temperaturas.append(num)
    soma += num
    tamanho = len(lista__de_temperaturas)
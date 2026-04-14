def quantidade(lista):
    return len(lista)


def media(lista):
    return sum(lista) / len(lista)


def maior_menor(lista):
    return max(lista), min(lista)


def pares_impares(lista):
    pares = 0
    impares = 0

    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

numeros = []

print("Digite números inteiros (0 para parar):")

while True:
    num = int(input())

    if num == 0:
        break

    numeros.append(num)

if len(numeros) == 0:
    print("Nenhum número foi digitado.")
else:
    print("\nQuantidade:", quantidade(numeros))
    print("Média:", media(numeros))

    maior, menor = maior_menor(numeros)
    print("Maior:", maior)
    print("Menor:", menor)

    pares, impares = pares_impares(numeros)
    print("Pares:", pares)
    print("Ímpares:", impares)
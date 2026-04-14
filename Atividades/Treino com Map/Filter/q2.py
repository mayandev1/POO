# 2. Um aplicativo registra temperaturas ao longo do dia. Desenvolva um programa que receba valores de
# temperatura informados pelo usuário. A entrada deve continuar até que um valor negativo seja digitado.
# Armazene os valores em uma lista e, ao final, calcule e exiba a média das temperaturas registradas.

lista__de_temperaturas = []
soma = 0
media = 0

print("Digite as temperaturas (valor negativo para parar):")

while True:
    num = float(input())

    if num < 0:
        media = soma/tamanho
        print(F"\nMedia das temperaturas registradas: {media}")
        print("Temperaturas:")
        print(lista__de_temperaturas)
        break

    lista__de_temperaturas.append(num)
    soma += num
    tamanho = len(lista__de_temperaturas)

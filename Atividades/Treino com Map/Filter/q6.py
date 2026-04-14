import random

def impares(num):
    if num % 2 == 1:
        return num
    else:
        return None

lista = []

quantidade = int(input("Digite o tamanho da lista: "))

while len(lista) < quantidade:
    num = random.randint(1, 100)
    
    if num not in lista:
        lista.append(num)
        
resultado = list(map(impares, lista))

impares = [x for x in resultado if x is not None]

print("Lista original:", lista)
print("Lista somente com números impares:", impares)
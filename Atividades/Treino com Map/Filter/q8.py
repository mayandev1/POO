import random

def eh_primo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def quadrado(x):
    return x ** 2

lista = []

quantidade = int(input("Digite o tamanho da lista: "))

while len(lista) < quantidade:
    num = random.randint(1, 100)
    
    if num not in lista:
        lista.append(num)
        
primos = list(filter(eh_primo, lista))
primos_ao_quadrado = list(map(quadrado, primos))

print("Lista original:", lista)
print("Lista de números primos:", primos)
print("Lista de números primos ao quadrado:", primos_ao_quadrado)
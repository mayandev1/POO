lista = []

while True:
    num = int(input("\nDigite um número inteiro (negativo para encerrar): "))
    
    if num < 0:
        break
    
    if num % 3 == 0:
        lista.insert(0, num)
    elif num % 5 == 0:
        lista.append(num)
    else:
        indice = len(lista) // 2
        lista.insert(indice, num)

print("\nLista original:", lista)

mult3 = []
mult5 = [] 
outros = []

for num in lista:
    if num % 3 == 0:
        mult3.append(num)
    elif num % 5 == 0:
        mult5.append(num)
    else:
        outros.append(num)

mult3.sort()
mult5.sort()
outros.sort()

nova_lista = mult3 + outros + mult5

print("Lista organizada:", nova_lista)
print("Ordem crescente:", sorted(lista))
print("Ordem decrescente:", sorted(lista, reverse=True))
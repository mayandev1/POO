lista = []

while True:
    num = int(input("\nDigite um número inteiro (negativo para encerrar): "))
    
    if num < 0:
        copia = lista.copy()
        
        print("Lista Original:", lista)
        print("Crescente:", sorted(copia))
        print("Decrescente:", sorted(copia, reverse=True))
        break
    
    if num % 3 == 0:
        lista.insert(0, num)
    elif num % 5 == 0:
        lista.append(num)
    else:
        indice = len(lista)//2
        lista.insert(indice, num)
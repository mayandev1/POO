qntTotal = 0

while True:
    num = int(input("Digite um numero inteiro positivo: "))
    
    if num < 0:
        break
    
    if num % 2 == 0:
        print("Par!")
    else:
        print("Impar!")
        
    qntTotal += 1
    
print("\nQuantidade de números positivos digitados:", qntTotal)
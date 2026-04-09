qntTotal = 0
somaPares = 0
maiorQue10 = 0
temNegativo = False

while True:
    num = int(input("Digite um numero (0 para encerrar): "))
    
    if num == 0:
        break
    
    qntTotal += 1
    
    if num > 10:
        maiorQue10 += 1
    
    if num % 2 == 0:
        somaPares += num
        
    if num < 0:
        temNegativo = True
        
print("\nRESULTADOS:")
print("Quantidade total de números:", qntTotal)
print("Soma dos pares:", somaPares)
print("Quantidade de números > 10:", maiorQue10)
print("Houve número negativo:", "SIM" if temNegativo else "NÃO")
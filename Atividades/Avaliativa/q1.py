def fatorial(N):
    resultado = 1
    for i in range(1, N + 1):
        resultado *= i
        
    print(f"O fatorial de {N} é {resultado}")
    return resultado

num = int(input("Digite um número inteiro para ver o seu fatorial:\n"))
    
fatorial(num)
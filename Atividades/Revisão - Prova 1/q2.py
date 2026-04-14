def transacoes():
    print("Todas as transações cadastradas: ", lista_transacoes)
    print(f"A maior transação foi no valor de {maior} reais.")
    print(f"A menor transação foi no valor de {menor} reais.")
    print(f"Soma total de todas as transações é de {total} reais.")
    print(f"{qnt_transacoes_maior100} foram maiores do que 100 reais.")
    
    if total <= 500:
        print("Uso baixo.")
    elif total > 500 and total <= 1500:
        print("Uso moderado.")
    else:
        print("Uso elevado.")
    

qnt_transacoes = int(input("Informe a quantidade de transações: "))

lista_transacoes = []
total = 0
qnt_transacoes_maior100 = 0

while len(lista_transacoes) < qnt_transacoes:
    try:
        num = float(input("Informe o valor da transação: "))
        
        if num <= 0:
            print("Digite um valor maior que 0!")
            continue
        
        lista_transacoes.append(num)
        total += num

    except ValueError:
        print("Erro! Digite um número válido.")
        
maior = lista_transacoes[0]
menor = lista_transacoes[0]

for num in lista_transacoes:
    if num > maior:
        maior = num
        
    if num < menor:
        menor = num

for num in lista_transacoes:
    if num > 100:
        qnt_transacoes_maior100 += 1
        
transacoes()
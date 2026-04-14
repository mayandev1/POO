def finalizacao():
    print("Nome do cliente: ", nome_cliente)
    print("Lista de compras realizadas:")
    print(lista_de_compras)
    print(f"Valor total gasto é igual a {total} reais.")
    print(f"Valor do limite restante é de {resto_do_limite} reais.")

nome_cliente = input("Digite o nome do cliente: ")
limite_cartao = float(input("Digite o limite do cartão: "))

lista_de_compras = []
total = 0
resto_do_limite = 0

while len(lista_de_compras) < 3:
    valor = float(input("Digite o valor das 3 compras: "))
    lista_de_compras.append(valor) 
    total += valor
    
resto_do_limite = limite_cartao - total

if total > limite_cartao:
    print("Limite de compra excedido!")
    print("Fechando o programa...")
    exit()
else:
    print("Compra dentro do limite.")
    finalizacao()
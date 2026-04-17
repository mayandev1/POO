# Muito ez, +2.5 score 

preco = 5.00
quantidade = 120
lucro = 400
lucro_max = lucro
custo_total = 200
preco_ingresso = 0
qnt_vendido = 0

while preco >= 1:
    print(f"Preço ingresso = {preco}, Quantidade = {quantidade}, Lucro = {lucro}")
    preco -= 0.50
    quantidade += 26
    lucro = (preco * quantidade) - custo_total
    
    if lucro > lucro_max:
        lucro_max = lucro
        preco_ingresso = preco
        qnt_vendido = quantidade
        
print("\nLucro máximo = ", lucro_max)
print("Preço do ingresso = ", preco_ingresso)
print("Quantidade vendida = ", qnt_vendido)
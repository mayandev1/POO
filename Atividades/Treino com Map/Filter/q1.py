lista_de_pontuacao = []

for num in range(5):
    num = int((input("Digite as 5 pontuações:\n")))
    lista_de_pontuacao.append(num)
    
print("Lista normal:")
print(lista_de_pontuacao)

print("\nLista organizada:")
lista_de_pontuacao.sort()
print(lista_de_pontuacao)

print("\nLista invertida:")
lista_de_pontuacao.reverse()
print(lista_de_pontuacao)

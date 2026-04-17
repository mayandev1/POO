# Aparentemente acertei, +2.5 score

def campeao(lista_nomes, lista_tempo):
    menor = lista_tempo[0]
    id = 0
    
    for num in lista_tempo:
        if num < menor:
            menor = num
            id = lista_tempo.index(num)
    print("Campeão = ", lista_nomes[id])
    print("Tempo total = ", menor)
            

qnt_corredor = int(input("Informe quantos corredores: "))
lista_nomes = []
lista_tempo = []
soma = 0
i = 1

while len(lista_nomes) < qnt_corredor:
    nome = input("Nome do corredor: ")
    lista_nomes.append(nome)
    
    for i in range(3):
        tempo = int(input("Digite os tempos de cada volta: "))
        soma += tempo
    lista_tempo.append(soma)
    soma = 0
    
campeao(lista_nomes, lista_tempo)
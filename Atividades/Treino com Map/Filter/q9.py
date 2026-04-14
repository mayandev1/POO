def maior_doq_4_digitos(nome):
    if len(nome) > 4:
        return nome
    
def converter_para_maiusculo(nome):
    return nome.upper()

lista_de_nomes = []

qnt = int(input("Quantos nomes quer digitar?\n"))

while len(lista_de_nomes) < qnt:
    nome = input("Digite um nome: ")
    lista_de_nomes.append(nome)
    
lista_nomes_maiores_Q4digitos = list(filter(maior_doq_4_digitos, lista_de_nomes))

lista_nomes_maiores_Q4digitos_Maiusculo = list(map(converter_para_maiusculo, lista_nomes_maiores_Q4digitos))

print("Lista de nomes original:")
print(lista_de_nomes)
print("Lista de nomes com mais de 4 digitos:")
print(lista_nomes_maiores_Q4digitos)
print("Lista de nomes com mais de 4 digitos, maiúscula:")
print(lista_nomes_maiores_Q4digitos_Maiusculo)
frutas = ["Maçã", "Uva", "Pera", "Salada Mista"]

while (True):
        
    nome_de_fruta = input("Digite de uma fruta (0 para encerrar): ")
    
    if nome_de_fruta == 0:
        break

    if nome_de_fruta in frutas:
        print("Fruta já cadastrada!\n")
    else:
        print("Fruta adicionada!\n")
        frutas.append(nome_de_fruta)
        print(frutas)
def trocar_cheque(valor):
    notas = [100, 50, 20, 10, 5, 2]
    resultado = {}

    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            resultado[nota] = quantidade
            valor = valor % nota

    return resultado, valor

valor = int(input("Digite o valor do cheque: "))

if valor <= 50:
    print("O valor deve ser maior que 50 reais.")
elif valor > 1000:
    print("O valor não pode ser maior que 1000 reais.")
else:
    resultado, resto = trocar_cheque(valor)

    if resto != 0:
        print("Não é possível trocar o seu cheque, entre com outro cheque!")
    else:
        print("Notas necessárias:")

        for nota in resultado:
            print(f"{resultado[nota]} nota(s) de {nota}")
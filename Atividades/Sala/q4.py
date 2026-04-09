saldo = 1000.0

while True:
    print("\n1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            saldo += valor
            print("Depósito realizado!")
        else:
            print("Valor inválido!")

    elif opcao == 3:
        valor = float(input("Digite o valor para saque: "))
        if valor <= 0:
            print("Valor inválido!")
        elif valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            print("Saque realizado!")

    elif opcao == 4:
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
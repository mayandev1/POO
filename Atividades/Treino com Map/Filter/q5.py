import random
import time
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def loading_cobrinha():
    largura = 30

    for i in range(largura + 1):
        limpar()
        
        barra = "█" * i + " " * (largura - i)
        
        print("🎲 REALIZANDO SORTEIO...\n")
        print(f"[{barra}]")
        
        time.sleep(0.05)

    print("\n✨ Finalizando...")
    time.sleep(0.5)


def menu():
    print("------ MENU DE SORTEIO ------")
    print("1. Definir intervalo dos números do sorteio")
    print("2. Definir quantidade de números a serem sorteados")
    print("3. Realizar sorteio")
    print("4. Exibir números já sorteados")
    print("5. Sair")


inicio = 0
fim = 0
qnt_nuns = 0
sorteados = []

while True:
    limpar()
    menu()
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        limpar()
        print("Digite o inicio e o fim do intervalo:")
        inicio = int(input())
        fim = int(input())

    elif opcao == 2:
        limpar()
        qnt_nuns = int(input("Informe quantos números deseja sortear: "))

    elif opcao == 3:
        if inicio == 0 and fim == 0:
            print("\n⚠️ Defina o intervalo primeiro!")
            input("\nPressione ENTER para continuar...")
            continue

        if qnt_nuns == 0:
            print("\n⚠️ Defina a quantidade primeiro!")
            input("\nPressione ENTER para continuar...")
            continue

        if qnt_nuns > (fim - inicio + 1):
            print("\n❌ Não é possível sortear sem repetir!")
            input("\nPressione ENTER para continuar...")
            continue

        loading_cobrinha()

        sorteados = []

        while len(sorteados) < qnt_nuns:
            num = random.randint(inicio, fim)
            
            if num not in sorteados:
                sorteados.append(num)

        limpar()

        print("🎉 SORTEIO FINALIZADO! 🎉")
        print("=" * 35)

        for num in sorteados:
            print(f"👉 Número sorteado: {num}")
            time.sleep(0.3)

        print("=" * 35)
        print("💖 PARABÉNS! 🍀")

        input("\nPressione ENTER para continuar...")

    elif opcao == 4:
        limpar()
        print("📋 Números já sorteados:\n")
        print(sorteados)
        input("\nPressione ENTER para continuar...")

    elif opcao == 5:
        print("Encerrando...\n")
        break

    else:
        print("Opção inválida, digite novamente!\n")
        input("Pressione ENTER para continuar...")
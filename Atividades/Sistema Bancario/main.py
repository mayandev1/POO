from datetime import datetime


class Conta:
    def __init__(self, numero_conta, nome_cliente, saldo, limite):
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return

        self.saldo += valor

        self.historico.adc_transacao(
            f"Depósito de R$ {valor:.2f}"
        )

        print("Depósito realizado com sucesso!")

    def extrato(self):
        print("\n===== EXTRATO =====")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Nome do cliente: {self.nome_cliente}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Limite disponível: R$ {self.limite:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return

        if valor > (self.saldo + self.limite):
            print("Saldo insuficiente.")
            return

        self.saldo -= valor

        self.historico.adc_transacao(
            f"Saque no valor de R$ {valor:.2f}"
        )

        print("Saque realizado com sucesso!")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Valor inválido para transferência.")
            return

        if valor > (self.saldo + self.limite):
            print("Saldo insuficiente.")
            return

        self.saldo -= valor

        conta_destino.saldo += valor

        self.historico.adc_transacao(
            f"Transferência de R$ {valor:.2f} para a conta {conta_destino.numero_conta}"
        )

        conta_destino.historico.adc_transacao(
            f"Transferência recebida de R$ {valor:.2f} da conta {self.numero_conta}"
        )

        print("Transferência realizada com sucesso!")


class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []

    def adc_transacao(self, mensagem):
        horario = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        self.transacoes.append(f"[{horario}] {mensagem}")

    def imprimir_historico(self):
        print("\n===== HISTÓRICO =====")
        print(
            f"Conta criada em: {self.data_abertura.strftime('%d/%m/%Y %H:%M:%S')}"
        )

        if len(self.transacoes) == 0:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.transacoes:
                print(transacao)


# main

conta1 = Conta(
    numero_conta=100,
    nome_cliente="Mayan",
    saldo=1000,
    limite=500
)

conta2 = Conta(
    numero_conta=101,
    nome_cliente="Prof Thiago",
    saldo=1000,
    limite=500
)

conta1.depositar(400)
conta2.depositar(600)

conta1.transferir(600, conta2)
conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()

conta1.historico.imprimir_historico()
conta2.historico.imprimir_historico()
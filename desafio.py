def print_extrato(saldo, extrato):
    print("Extrato".center(20, "="))
    s = f"R$ {saldo:.2f}"
    for item in extrato:
        print(f"{item[0]:<15}{item[1]}R${item[2]: .2f}")
    print(f"Saldo: {s:>18}")
    print("".center(25, "="))


if __name__ == "__main__":

    menu = f"""

    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair
"""
    LIMITE_DIARIO = 500
    LIMITE_MAXIMO_SAQUES_DIARIOS = 3

    limite_diario_utilizado = 0
    saldo = 0
    quantidade_saques = 0
    extrato = []

    while True:
        opcao = input(menu)
        if opcao == "d":
            valor_deposito = float(input("Digite o valor do depósito: R$ "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato.append(("Entrada", "+", valor_deposito))
            else:
                print("Valor inválido.")
        elif opcao == "s":

            valor_saque = float(input("Digite o valor para sacar R$: "))

            if (quantidade_saques + 1) > LIMITE_MAXIMO_SAQUES_DIARIOS:
                print("Quantidade de saques diários excedido.")
            elif valor_saque > LIMITE_DIARIO:
                print("Limite para o saque excedido")
            elif (valor_saque > saldo):
                print("Saldo insuficiente")
            else:
                saldo -= valor_saque
                quantidade_saques += 1
                extrato.append(("Saída", "-", valor_saque))

        elif opcao == "e":
            print_extrato(saldo, extrato)

        elif opcao == "q":
            break
        else:
            print("Opção inválida")

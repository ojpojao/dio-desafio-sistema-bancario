import colorama
import textwrap
from os import system, name

from colorama import Fore, Style

colorama.init(autoreset=True)

def clear() -> None:
    command = ""
    if name == "nt":
        command = "cls"
    else:
        command = "clear"
    system(command)

def visualizar_historico(saldo, /, *, extrato):
    clear()
    print(Fore.CYAN + "Extrato".center(20, "=") + Fore.RESET)
    s = f"R$ {saldo:.2f}"
    for item in extrato:
        print(f"{item[0]}\t\t{item[1]}R${item[2]: .2f}")
    print()
    print(f"Saldo:\t\tR$ {saldo:.2f}")


def sacar(
    saldo,
    valor_saque,
    extrato,
    limite_valor_diario_por_saque,
    quantidade_saques_diarios,
    limite_diario_saques,
):
    if valor_saque > saldo:
        print(Fore.YELLOW + "Saldo insuficiente")
    elif valor_saque > limite_valor_diario_por_saque:
        print(Fore.YELLOW + f"Limite por saque é de R$ {limite_valor_diario_por_saque }.")
    elif (quantidade_saques_diarios + 1) > limite_diario_saques:
        print(Fore.YELLOW + f"Limite de {quantidade_saques_diarios} saques diários excedido.")
    else:
        saldo -= valor_saque
        quantidade_saques_diarios += 1
        extrato.append(("Saída", f"{Fore.LIGHTRED_EX}-", valor_saque))

        print(Fore.LIGHTGREEN_EX + "Operação realizada com sucesso!")


    return saldo, quantidade_saques_diarios, extrato


def depositar(saldo, valor_deposito, extrato, /):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(("Entrada", f"{Fore.GREEN}+", valor_deposito))
        print(Fore.GREEN + "Operação realizada com sucesso!")
    else:
        print(Fore.RED + "Operação não realizada! Valor inválido.")
    return saldo, extrato


def filtrar_usuario(cpf: str, usuarios: list) -> dict:
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            return usuario
    return {}


def criar_usuario(usuarios):

    cpf = input("Informe o numero do CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(Fore.RED +"CPF já está cadastrado!!!!")
        return
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento(ddmmaaaa): ")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append(
        {
            "nome": nome,
            "endereco": endereco,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
        }
    )
    mensagem_sucesso = Fore.GREEN + "Usuário cadastrado com sucesso"
    print(len(mensagem_sucesso) * "*")
    print(mensagem_sucesso)

def listar_contas(contas):
    clear()
    if len(contas) == 0:
        print(Fore.LIGHTRED_EX + "Nenhuma conta cadastrada")
        return
    for conta in contas:
        agencia = f"{"Agência:\t":>10}{conta["agencia"]}"
        conta_corrente = f"{"C/C:\t":>10}{conta["numero_conta"]}"
        titular = f"{"Titular:\t":>10}{conta["usuario"]["nome"]}"
        linha = f"""\
{agencia}
{conta_corrente}
{titular}
    """
        print("=" * 20)
        print(linha)


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(Fore.GREEN + "Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print(Fore.RED + "Não foi possivel criar conta. Usuário não encontrado.\nFluxo de criação de conta encerrado.")


def menu():
    cabecalho = Fore.CYAN + "Menu".center(20, "=") + Fore.RESET
    menu = f"""
{cabecalho}
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[nu]\tNovo usuário
[lc]\tListar Conta
[q]\tSair

"""
    return input(textwrap.dedent(menu))


if __name__ == "__main__":

    LIMITE_VALOR_DIARIO_POR_SAQUE = 500
    LIMITE_MAXIMO_SAQUES_DIARIOS = 3
    AGENCIA = "0001"

    saldo = 0
    quantidade_saques = 0
    extrato = []

    contas = []
    clientes = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor_deposito = float(input("Digite o valor do depósito: R$ "))
            saldo, _ = depositar(saldo, valor_deposito, extrato)
        elif opcao == "s":
            valor_saque = float(input("Digite o valor para sacar R$: "))
            saldo, quantidade_saques, extrato = sacar(
                saldo,
                valor_saque,
                extrato,
                limite_valor_diario_por_saque=LIMITE_VALOR_DIARIO_POR_SAQUE,
                quantidade_saques_diarios=quantidade_saques,
                limite_diario_saques=LIMITE_MAXIMO_SAQUES_DIARIOS,
            )
        elif opcao == "e":
            visualizar_historico(saldo, extrato=extrato)
        elif opcao == "nc":
            numero_conta = str(len(contas) + 1).zfill(8)
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)
        elif opcao == "nu":
            criar_usuario(clientes)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print(Fore.RED + "Opção inválida")

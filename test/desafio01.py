# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_medio: float) -> str:

# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
    planos = {
        "Plano Essencial Fibra - 50Mbps": 0 < consumo_medio <= 10,
        "Plano Prata Fibra - 100Mbps": 10 < consumo_medio <= 20,
        "Plano Premium Fibra - 300Mbps": 20 < consumo_medio,
    }

    for key, value in planos.items():
        if value:
# TODO: Retorne o plano de internet adequado:
            return key

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
# recomendar_plano(consumo)

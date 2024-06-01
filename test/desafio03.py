# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


# TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number: str) -> str:

    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = r"^\(\d{2}\)\s9\d{4}-\d{4}$"
    # A função 're.match()' para verificar se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
        return "Número de telefone válido."
    else:
        # TODO: Crie um else e return, caso não o número de telefone seja inválido:
        return "Número de telefone inválido."


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)
# # Imprime o resultado:
print(result)

# numeros_telefones = [
#     "(62) 3570-9254",
#     "(68) 92277-1433",
#     "(96) 2465-4045",
#     "(68) 3553-7960",
#     "(51) 93415-6357",
#     "(86) 53627-8883",
#     "(88) 98888-8888",
#     "(11)91111-1111",
#     "225555-555",
#     "(99) 91111-1111"
# ]

# for numero_telefone in numeros_telefones:
#     result = validate_numero_telefone(numero_telefone)
#     print(f"{numero_telefone} é um {result}")

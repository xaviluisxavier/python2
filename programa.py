# isto é um comentário

"""
Este programa implementa funções ortméticas
"""


def aritmetica(valor1, valor2, op='+'):
    """
    Esta função inplementa as operações de somar, subtrair, multiplicar e dividir
    :param valor1: Primeiro fator de operação
    :param valor2: Segundo fator de operação
    :param op: Operação; valores validos são: + - : *
    :return: Resultado da operação
    """
    total = "Código de operação inválido"
    if op == '+':
        total = valor1 + valor2

    if op == '-':
        total = valor1 - valor2

    if op == '/':
        total = valor1 / valor2

    if op == '*':
        total = valor1 * valor2

    return total


if __name__ == '__main__':
    nome = input("Como te chamas? ")
    while True:
        fator1 = float(input("Insira o primeiro numero: "))
        fator2 = float(input("insira o segundo numero: "))
        operacao = input("insira a operação [+ , - , :, *] ")
        print(f' Olá {nome}, {fator1} {operacao} {fator2} = {aritmetica(fator1, fator2, operacao)}')
        continuar = input('Repetir [s | n]?  ')
        if continuar == 'n':
            break
    print(f'Adeus {nome}!')

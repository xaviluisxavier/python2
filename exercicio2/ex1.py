"""
1. Escreva um programa em Python que pede ao utilizador que lhe forneça
dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).
O seu programa deve gerar uma interação como a seguinte:
Vou pedir-lhe dois numeros
Escreva o primeiro numero, x = 5
Escreva o segundo numero, y = 6
O valor de (x + 3 * y) * (x - y) e: -23
"""


def operacao(valor1, valor2):
    operacao = (valor1 + 3 * valor2) * (valor1 - valor2)

    return operacao


if __name__ == '__main__':
    print('Vou pedir-lhe dois numeros')
    print()

    x = int(input(f'Digite o primeiro numero: '))
    y = int(input(f'Digite o segundo numero: '))

    print(f'({x} + 3 × {y}) × ({x} - {y}) = {operacao(x, y)}')



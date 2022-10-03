"""
1. Escreva um programa em Python que pede ao utilizador que lhe forneça
dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).
O seu programa deve gerar uma interação como a seguinte:
Vou pedir-lhe dois numeros
Escreva o primeiro numero, x = 5
Escreva o segundo numero, y = 6
O valor de (x + 3 * y) * (x - y) e: -23
"""

x = 0
y = 0
c = (x + 3 * y) * (x - y)

if __name__ == '__main__':
    print('Vou pedir-lhe dois numeros')
    print()
    x = input(f'Escreva o primeiro numero: ')
    y = input(f'Escreva o segundo numero: ')

    print(f'O valor de ({x} + 3 * {y}) * ({x} - {y}) é: {c}')


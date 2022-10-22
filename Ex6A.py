"""
Escreva um programa que lê um inteiro e calcula o produto dos seus dígitos.
Exemplo: 342 -> 24
"""


def ler_numero(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print('O valor inserido não é um múmero. Tente de novo.')
    return num


if __name__ == '__main__':
    while True:
        numero = str(ler_numero('Insira um número: '))
        produto = 1
        for n in numero:
            produto *= int(n)
        print(f'O produto dos números {numero} é {produto}')
        if input('Correr de novo [s/n]? ') != 's':
            break

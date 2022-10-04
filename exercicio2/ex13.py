"""
13. Escreva um programa em Python que pede ao utilizador que lhe forneça
um número e que escreve a tabuada da multiplicação para esse número.
O seu programa deve gerar uma interacção como a seguinte:
Escreva um numero para eu escrever a tabuada da multiplicação
Num -> 8
8 x 1=8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
"""


def cal(valor):
    for x in range(1, 11):
        mult = valor * x
        print(f'{valor} × {x} = {mult}')


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Qual é o número? '))

            cal(num)

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print("Valor invalido")

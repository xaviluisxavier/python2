"""
16. Escreva um programa que lê um número e cria uma capicua cuja primeira
metade é o número lido. Por exemplo:
Escreva um número
-> 347
347743
"""


def numero(valor):
    valor = str(valor)
    numero = valor + valor[::-1]

    return numero


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Qual é o número? '))

            print(f'O número é {numero(num)}.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite uma valor válido')


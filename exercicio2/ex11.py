"""
11. Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
"""
def numero(valor):
    valor = str(valor)
    numero = valor[::-1]

    return numero


if __name__ == '__main__':

        num = int(input('Qual é o número? '))

        print(f'O número invertido é {numero(num)}.')

"""
10. Escreva um programa em Python que lê um número inteiro positivo e
calcula o número obtido do número lido que apenas contém os seus dígitos
impares. Por exemplo,
Escreva um inteiro
? 785554
Resultado: 7555
"""


def impar(num):
    num = int(num)
    if num % 2 != 0:
        return num
    else:
        return ''


if __name__ == '__main__':

    num = int(input('Digite um número inteiro: '))
    num = str(num)
    num_impar = ''

    for x in num:
        num_impar += str(impar(x))
    print(f'Resultado: {num_impar}')

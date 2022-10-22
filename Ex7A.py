"""
Escreva um programa em Python que lê um número inteiro positivo e produz o menor número que se pode
formar com esses dígitos. Por exemplo: 3475 -> 3457
"""


def ordenar(lista):
    while True:
        troquei = False
        for x in range(len(lista) - 1):
            if lista[x] > lista[x + 1]:
                temp = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = temp
                troquei = True
        if not troquei:
            break
    return lista


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
        caracteres = []
        for n in numero:
            caracteres.append(n)
        caracteres = ordenar(caracteres)
        print(''.join(caracteres))
        if input('Correr de novo [s/n]? ') != 's':
            break

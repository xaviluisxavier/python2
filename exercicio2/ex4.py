"""
- Um programa que lê um número inteiro correspondente a um certo número de segundos e que escreve
o número de dias, horas, minutos, segundos correspondentes a esse número. Por exemplo:
    * Escreve o número de segundos 345678
    * dias : 4 horas: 0 mins: 1 segs: 18
"""


def dia(valor):
    dias = valor / 60
    dias = dias / 60
    dias = dias / 24

    return dias


def horas(valor):
    horas = valor % (24 * 3600)
    horas = horas // 3600

    return horas


def min(valor):
    mins = valor % (24 * 60)
    mins = mins // 60

    return mins


def seg(valor):
    segs = valor
    segs %= 60

    return segs


if __name__ == '__main__':
    segundos = int(input('Quantos segundos? '))

    print(
        f'dias: {int(dia(segundos))} hours: {int(horas(segundos))} mins: {int(min(segundos))} segs: {int(seg(segundos))}')

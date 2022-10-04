"""
3- Um programa que pede ao utilizador que lhe forneça um inteiro correspondente a
um número de segundos e que calcula o número de dias correspondentes a esse número
de segundos.
    * Escreve um número de segundos
    * Exemplo - 65432998
    * O número de dias correspondentes é 757.3263657407407
"""


def operacao(valor):
    """
    segundos = 86400
    minutos = segundos / 60
    horas = minutos / 60
    dias = horas / 24
    """
    valor = valor / 60
    valor = valor / 60
    valor = valor / 24

    return valor


if __name__ == '__main__':
    segundos = int(input('Quantos segundos? '))

    print(f'Os {segundos} segundos equivalem a {operacao(segundos)} dias.')

"""
Complete o programa
Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""
import random


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """

    return random.randrange(ini, fim + 1)


def par(num):
    if num % 2 == 0:
        return num


if __name__ == '__main__':
    num_ini = int(input('Qual é o número inicial? '))
    num_end = int(input('Qual é o número final? '))
    opcao = int(input('Qual é a opção (1 - pares, 2 = impares, 3 - primos)'))

    for x in range(num_ini, num_end + 1):
        print(f'{get_random(num_ini, num_end)}', end=' ')
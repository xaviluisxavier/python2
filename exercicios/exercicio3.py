
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

    x = random.randint(ini, fim)

    return random.randrange(ini, fim + 1)


def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros + 1

    return zeros


if __name__ == '__main__':  # isto é o ponto de partida
    intervalo1 = int(input(f'Qual o inicio do intervalo?'))
    intervalo2 = int(input(f'Onde termnina o intervalo?'))
    operação = input(f'Deseja ver os números pares , os números impares ou os números primos?')
    primos = 0
    pares = 0
    impares = 0
    for n in range(intervalo1, intervalo2 + 1):
        if divisores(n) == 2:
            print(n)
            primos += 1

    print(f'Ola entre o intervalo {intervalo1} e {intervalo2}')

    x = random.randint(intervalo1, intervalo2)

    print(x)
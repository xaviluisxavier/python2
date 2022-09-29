import random


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0]
    estrelas = [0, 0]
    for x in range(len(nums)):
        while True:
            numero = get_random(1, 50)
            if numero not in nums:
                nums[x] = numero
                break
    for x in range(len(estrelas)):
        while True:
            numero = get_random(1, 12)
            if numero not in estrelas:
                estrelas[x] = numero
                break

    print(nums)
    print(estrelas)

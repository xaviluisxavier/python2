import random


def get_random(ini, fim):
    return random.randrange(ini, fim + 1)


def organizador(lista):
    for x in range(len(lista)):
        for i in range(x + 1, len(lista)):
            if lista[x] > lista[i]:
                lista[x], lista[i] = lista[i], lista[x]
    return lista


if __name__ == '__main__':
    numeros_randoms = [0, 0, 0, 0, 0]
    estrela = [0, 0]
    for x in range(5):
        for x in range(len(numeros_randoms)):
            while True:
                numero = get_random(1, 50)
                if numero not in numeros_randoms:
                    numeros_randoms[x] = numero
                    break
        for x in range(len(estrela)):
            while True:
                numero = get_random(1, 12)
                if numero not in estrela:
                    estrela[x] = numero
                    break

        print(f' Os 5 numeros são: {organizador(numeros_randoms)}')
        print(f' As 2 estrelas são: {organizador(estrela)}')

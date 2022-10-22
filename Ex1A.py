"""
Programa compara a idade de 3 amigos e diz qual é a idade do mais novo e a do mais velho.
O programa pede a idade do primeiro, a idade do segundo e a idade do terceiro.
Alguns exemplos de idades possivels para o primeiro, segundo, terceiro, assim como a resposta do programa:
10, 10, 10 - A idade do mais novo é 10, A idade do mais velho é 10.
10, 20, 20 - A idade do mais novo é 10, A idade do mais velho é 20.
10, 20, 30 - A idade do mais novo é 10, A idade do mais velho é 30.
20, 20, 30 - A idade do mais novo é 10, A idade do mais velho é 30.

Idealmente o programa deve perguntar se o utilizador desejar repetir e só terminar caso não deseje.
"""

AMIGOS = 3


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
        idades = []
        for x in range(AMIGOS):
            idade = ler_numero(f'Insira a idade do amigo {x + 1}: ')
            idades.append(idade)
            if x == 0:
                velho = idades[x]
                novo = idades[x]
            else:
                if idades[x] > velho:
                    velho = idades[x]
                if idades[x] < novo:
                    novo = idades[x]

        print(f'A idade do mais novo é {novo} e a idade do mais velho é {velho}.')
        if input('Correr de novo [s/n]? ') != 's':
            break
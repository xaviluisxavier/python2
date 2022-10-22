"""
Este programa compara a idade de 3 amigos com idades diferentes e diz qual é o nome do mais novo e o nome do mais velho
O programa pede o nome e a idade do primeiro, do segundo e do terceiro

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
        nomes = []
        idades = []
        for x in range(AMIGOS):
            nome = input('Insira o nome: ')
            while True:
                idade = ler_numero(f'Insira a idade para {nome}: ')
                if idade not in idades:
                    nomes.append(nome)
                    idades.append(idade)
                    break
                else:
                    print(f'A idade {idade} já foi inserida. Insira uma idade diferente.')
            if x == 0:
                velho = idades[x]
                novo = idades[x]
            else:
                if idades[x] > velho:
                    velho = idades[x]
                if idades[x] < novo:
                    novo = idades[x]

        print(f'Mais novo com {novo} anos de idade:')
        for x in range(len(idades)):
            if idades[x] == novo:
                print(nomes[x])

        print(f'Mais velho com {novo} anos de idade:')
        for x in range(len(idades)):
            if idades[x] == velho:
                print(nomes[x])
        if input('Correr de novo [s/n]? ') != 's':
            break

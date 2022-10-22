"""
Escreve um programa que será utilizado para encriptar mensagens. O programa usa uma lista de duas dimensões conforme se
exemplifica.

chave = [
            ['123AaboPul '],
            ['APuo1lba3 2']
        ]

Exemplo da interação do programa com o utilizador para encriptar:

Insira a primeira parte da chave sem repetir caracteres: 123AaboPul [atenção que há um espaço no último caracter]
Insira a segunda parte da chave: uyTkK567OaH
Deseja encriptar (1) ou descriptar (2)? 1
Insira a mensagem: Olá, bom dia 3!
O programa apresenta a mensagem encriptada: O á,2lbm2di12u!

Exemplo da interação do programa com o utilizador para descriptar:
Insira a primeira parte da chave sem repetir caracteres: 123AaboPul [atenção que há um espaço no último caracter]
Insira a segunda parte da chave: uyTkK567OaH
Deseja encriptar (1) ou descriptar (2)? 2
Insira a mensagem encriptada: OaáH56mHDiKHT!
O programa apresenta a mensagem descriptada: Olá, bom dia 3!


Possíveis mensagems de erro:

Chave contém caracteres duplicados
Segunda parte da chave não tem o mesmo número de caracteres que a primeira
"""
import random


def baralhar(word):
    return ''.join(random.sample(word, len(word)))


def ler_numero(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print('O valor inserido não é um múmero. Tente de novo.')
    return num


def obter_chave(msg):
    while True:
        parte = input(msg)
        for x in range(len(parte)):
            total = 0
            for y in range(len(parte)):
                if parte[x] == parte[y]:
                    total += 1
        if total > 1:
            print('Não pode conter caracteres duplicados. Tente de novo.')
        else:
            break
    return parte


def diferentes(parte1, parte2):
    for c in parte1:
        if c not in parte2:
            return True
    return False


if __name__ == '__main__':
    while True:
        chave = []

        parte1 = obter_chave('Insira a primeira parte da chave sem repetir caracteres:')
        while True:
            parte2 = obter_chave('Insira a segunda parte da chave sem repetir caracteres:')
            if len(parte1) != len(parte2) or diferentes(parte1, parte2):
                print('A segunda parte tem de ter os caracteres que a primeira numa ordem diferente. Tente de novo.')
            else:
                break

        chave.append(parte1)
        chave.append(parte2)

        processo = ler_numero('Deseja encriptar (1) ou descriptar (2)? ')
        if processo == 1:
            texto = 'encriptar'
        else:
            texto = 'descriptar'
        mensagem = input(f'Insira a mensagem para {texto}: ')

        resultado = []
        if processo == 1:
            for c in mensagem:
                for x in range(len(chave[0])):
                    if c == chave[0][x]:
                        c = chave[1][x]
                        break
                resultado.append(c)
        else:
            for c in mensagem:
                for x in range(len(chave[1])):
                    if c == chave[1][x]:
                        c = chave[0][x]
                        break
                resultado.append(c)

        resultado = ''.join(resultado)
        print(f'A mensagem {mensagem} encriptada fica assim: {resultado}')
        if input('Correr de novo [s/n]? ') != 's':
            break

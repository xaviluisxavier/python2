"""
Escreva um programa que lê uma frase e apresenta quantas vezes há cada caracter minúsculo.
"""


if __name__ == '__main__':
    while True:
        minuscula = {}
        testo = input('Escreve uma frase:\n')
        for t in testo:
            if t == t.lower() and t.isalpha():
                if t not in minuscula.keys():
                    minuscula[t] = 1
                else:
                    minuscula[t] += 1
        for m in minuscula:
            print(f'{m} = {minuscula.get(m)}')
        if input('Correr de novo [s/n]? ') != 's':
            break

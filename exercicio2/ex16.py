"""
16. Escreva um programa que lê um número e cria uma capicua cuja primeira
metade é o número lido. Por exemplo:
Escreva um número
-> 347
347743
"""

if __name__ == '__main__':
    num = input('introduza um numero: ')
    inver = []
    inver1 = []
    cont = len(num)
    for x in range(len(num)):
        cont -= 1
        inver.append(num[cont])
    print(f'{num}{"".join((inver))}')


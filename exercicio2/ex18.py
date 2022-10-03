"""
18. Escreva um programa que lê um número inteiro e determina quantas vezes
aparecem dois zeros seguidos. Por exemplo:
Escreva um inteiro
? 98007640003
O numero tem 3 zeros seguidos
"""

def countZeros(numero):
    count = 0;
    while numero % 10 == 0:
        count += 1
        numero /= 10
    return count


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Digite o número inicial: '))

            print(f'O número {num} tem {countZeros(num)} zeros.')

            continuar = input('Repetir [s | n]? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')
"""
14. Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
"""

def digito(valor):
    digitos = len(str(valor))

    return digitos


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Qual é o número? '))

            print(f'O número {num} contém {digito(num)} digitos.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')


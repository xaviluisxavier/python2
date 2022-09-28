def maior(num1, num2):
    if num1 > num2:
        print(f'numero {num1} é maior')


def menor(num1, num2):
    if num1 < num2:
        print(f'numero {num1} é menor')


def igual(num1, num2):
    if num1 == num2:
        print(f'numero {num1} é igual ao {num2}')


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        primeiro_n = int(input('Insira o primeiro numero '))
        segundo_n = int(input('Insira o segundo numero '))
        if primeiro_n > segundo_n:
            print(maior(primeiro_n,segundo_n))
        if primeiro_n < segundo_n:
            print(menor(primeiro_n,segundo_n))
        if primeiro_n == segundo_n:
            print(igual(primeiro_n,segundo_n))

        continuar = input('Repetir [s | n]? ')
print(f'Adeus!')



if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        primeiro_n = int(input('Insira o primeiro numero '))
        segundo_n = int(input('Insira o segundo numero '))
        if primeiro_n > segundo_n:
            print(f'O numero {primeiro_n} é maior')
        if primeiro_n < segundo_n:
            print(f'O numero {primeiro_n} é menor')
        else:
            print(f'o numero {primeiro_n} é igual ao numero {segundo_n}')

        continuar = input('Repetir [s | n]? ')
print(f'Adeus!')

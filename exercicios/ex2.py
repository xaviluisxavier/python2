def comfor(num1, num2):
    soma = 0
    for n in range(num1, num2 + 1):
        soma += n

    return soma


def comwhile(num1, num2):
    soma = 0
    n = 0
    while n < (num1, num2 + 1):
        soma += n
        n += 1
    return soma


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        primeiro_n = int(input('Insira o primeiro numero '))
        segundo_n = int(input('Insira o segundo numero '))
        fuc = input(' Usar comwhile ou comfor?')

        while True:

            if fuc == 'comfor':
                print(comfor(primeiro_n, segundo_n))
                break
            elif fuc == 'comwhile':
                print(comwhile(primeiro_n, segundo_n))
                break
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')

def comfor(num1, num2):
    soma = 0
    for n in range(0, (num2 - num1) + 1):
        soma += num1 + n

    return soma


def comwhile(num1, num2):
    soma = 0
    n = 0
    while n < (num2 - num1) + 1:
        soma += num2 - n
        n += 1

    return soma


if __name__ == '__main__':
    primeiro_n = int(input('Insira o primeiro numero '))
    segundo_n = int(input('Insira o segundo numero '))
    fuc = input(' Usar comwhile ou comfor?')

    while True:

        if fuc == 'comfor':
            print(comfor(primeiro_n, segundo_n))
            break
        if fuc == 'comwhile':
            print(comwhile(primeiro_n, segundo_n))
            break

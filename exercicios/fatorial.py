def fatorial(num):
    resultado = 1
    while num > 1:
        resultado *= num
        num -= 1

    return resultado


if __name__ == '__main__':
    numero = int(input("Fatorial de: "))
    print(fatorial(numero))

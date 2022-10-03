def parouimpar(num):
    if (num % 2) == 0:
        return f'O seu {num} é par'
    else:
        return f'O seu {num} é impar'
    if num == 0:
        return f'erro'


if __name__ == '__main__':
    while True:
        numero = float(input("Insira o numero: "))
        print(parouimpar(numero))
        continuar = input('Repetir [s | n]?  ')
        if continuar == 'n':
            break

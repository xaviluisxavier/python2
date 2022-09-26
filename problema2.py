"""
Pede ao utilizador um numero inicial.
Pede ao utilizador um numero que representa "quantos".
Mostra aquela quantidade de numeros primos a partir do numero inicial.
"""

def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        ini = int(input('Insira o número inicial: '))
        quantos = int(input('Insira a quatnidade:  '))
        primos = 0
        for n in range(ini, quantos + 1):
            if divisores(n) == 2:
                primos += 1
        print(f'A partir de {ini} até há quantidade pedida {quantos} há {primos} de primos.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')


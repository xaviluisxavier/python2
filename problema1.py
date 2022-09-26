"""
Pede ao utilizador 2 numeros. O 2º numero deve ser >= 1º.
Mostra todos os numeros primos;
Depois de mostrar os numeros diz quantos numeros primos havia.
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
        ini = int(input('Insira o número inicial '))
        fim = int(input('Insira o número final '))
        primos = 0
        # alterar o for para um while
        for n in range(ini, fim + 1):
            if divisores(n) == 2:
                primos += 1
        print(f'Entre {ini} e {fim} há {primos} de primos.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')
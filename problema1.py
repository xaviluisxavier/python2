"""
Pede ao utilizador 2 numeros. O 2º numero deve ser >= 1º.
Mostra todos os numeros primos;
Depois de mostrar os numeros diz quantos numeros primos havia.
"""


def numeros(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input("Insira o primeiro numero: "))
        num2 = int(input("insira o segundo numero: "))

        if num2 >= num1:
            print(f'Numeros primos: {num2} ')


        continuar = input('Repetir [s | n]?  ')
    print(f'Adeus!')

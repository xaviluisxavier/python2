"""
Imprimiar os numeros pares entre 1 e o numero inserido
"""
from programa3 import parouimpar
# range(start, stop, step)


if __name__ == '__main__':

    num1 = int(input("Insira o primeiro numero: "))

    for x in range(1, num1 + 1):

        print(parouimpar(x))

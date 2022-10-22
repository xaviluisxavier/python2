"""
Use exclusivamente ciclos while

Este programa começa por gerar 9 numeros aleatórios entre 10 e 90 inclusive e guarda-os numa lista de 9 casas, mas
apenas se os números forem divisíveis por 10.
O programa depois imprime:
Soma de todas as casas:
Menor valor entre todas as casas:
Maior valor entre todas as casas:
"""
import random

if __name__ == '__main__':
    while True:
        casas = []
        total = 0
        for x in range(9):
            while True:
                num = random.randrange(10, 90 + 1)
                if num % 10 == 0:
                    break

            if x == 0:
                menor = num
                maior = num
            else:
                if num < menor:
                    menor = num
                if num > maior:
                    maior = num

            total += num
            casas.append(num)

        print(casas)
        print(f'Soma: {total} Menor: {menor} Maior: {maior}')
        if input('Correr de novo [s/n]? ') != 's':
            break

"""
Use exclusivamente ciclos for

O programa pergunta ao utilizador se quer apenas números únicos.
Gera 9 numeros aleatórios entre 10 e 90 inclusive e guarda-os numa lista de 9 casas, mas
apenas se os números forem divisíveis por 10 e se forem unicos, caso o utilizador assim deseje

O programa mostra:
Soma de todas as casas: xxxx
Menor valor entre todas as casas: xxxx
Maior valor entre todas as casas: xxxx
Quantas casas têm números únicos: xxxx (Por exemplo se a 2ª casa tem 10, a 5ª casa tem 20 e todos as outras casas têm 30
então a resposta seria 2.
"""

import random

if __name__ == '__main__':
    temp1 = [1]
    for t1 in temp1:
        temp1.append(1)
        unicos = input('Pretende apenas números únicos (s/n) ')
        if unicos == 's':
            unicos = True
        else:
            unicos = False

        casas = []
        total = 0
        for x in range(9):
            temp2 = [1]
            for t in temp2:
                temp2.append(1)
                num = random.randrange(10, 90 + 1)
                if num % 10 == 0:
                    if unicos:
                        if num not in casas:
                            break
                    else:
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

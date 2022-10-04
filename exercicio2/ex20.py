"""
20. Escreva um programa em Python escreve o seguinte:
1 x 8 + 1 = 9
12 x 8 + 2 = 98
123 x 8 + 3 = 987
1234 x 8 + 4 = 9876
12345 x 8 + 5 = 98765
123456 x 8 + 6 = 987654
1234567 x 8 + 7 = 9876543-
12345678 x 8 + 8 = 98765432
123456789 x 8 + 9 = 987654321
Os valores do primeiro termo da multiplicação e o resultado devem ser
calculados pelo seu programa.
"""


def cal(valor1, valor2):
    produto = 8
    st = ''
    for x in range(valor1, valor2):
        st += str(x)
        cals = int(st) * produto + x
        print(f'{st} × {produto} + {x} = {cals}')


if __name__ == '__main__':
    while True:
        num_inicial = 1
        num_final = 10

        cal(num_inicial, num_final)

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break

"""
11. Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
"""

if __name__ == '__main__':
    while True:
        try:
            num = input('Digite um numero: ')
            numstr = str(num)
            tm = len(numstr)
            strfim = ''

            for i in range(0, tm):
                tm -= 1
                strfim += numstr[tm]
            print(strfim)

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break
        except ValueError:
            print("Valor invalido")

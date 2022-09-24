"""
Pede ao utilizador um numero inicial.
Pede ao utilizador um numero que representa "quantos".
Mostra aquela quantidade de numeros primos a partir do numero inicial.
"""

if __name__ == '__main__':
    numero_prim = 0
    continuar = 's'
while continuar == 's':
    inicio = int(input('Insira o numero inicial: '))
    qnt_primos = int(input('Insira quantidade de primos: '))

    for n in range(inicio, 100):
        if numero_prim < qnt_primos:
            if n > 1:
                for j in range(qnt_primos, n):
                    if n % j == 0:
                        break
                else:
                    print(n)
                    numero_prim += 1
        else:
            break
print(f'Adeus')

"""
Pede ao utilizador um numero inicial.
Pede ao utilizador um numero que representa "quantos".
Mostra aquela quantidade de numeros primos a partir do numero inicial.
"""


if __name__ == '__main__':
 numero_prim = 0
 continuar = 's'
while continuar == 's':
    inicio = int(input('Insira o primeiro numero: '))
    fim = int(input('Insira o segundo numero: '))

    for n in range(inicio, fim + 1):
        if n > 1:
            for j in range(2, n):
                if n % j == 0:
                    break
            else:
                print(n)
                numero_prim += numero_prim 
    print(numero_prim)
    continuar = input('repetir [s | n]?')
print(f'Adeus')

"""
Pede ao utilizador 2 numeros. O 2º numero deve ser >= 1º.
Mostra todos os numeros primos;
Depois de mostrar os numeros diz quantos numeros primos havia.
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
                numero_prim += 1
    print(f'Quantidade de numeros primos:{numero_prim}')
    continuar = input('repetir [s | n]?')
print(f'Adeus')

"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
— Total das vendas
— O menor valor inserido
— O maior valor inserido
— A média das vendas
"""

if __name__ == '__main__':

    vendas = [0, 0, 0, 0, 0]
    ilhas = ['Faial', 'Pico', 'S. Jorge', 'Graciosa', 'Terceira']

    venda_total = 0
    venda_menor = 0
    venda_maior = 0

    for x in range(0, len(ilhas)):
        vendas[x] = int(input(f'Vendas {ilhas[x]}: '))
        venda_total += vendas[x]

    venda_menor = vendas[0]
    venda_maior = vendas[0]

    for x in range(0, len(vendas)):
        if vendas[x] > venda_maior:
            venda_maior = vendas[x]
        if vendas[x] < venda_menor:
            venda_menor = vendas[x]

    print(f'Total de vendas: {venda_total}')
    print(f'A menor venda é: {venda_menor}')
    print(f'A maior venda é: {venda_maior}')
    print(f'A média é: {venda_total / len(ilhas)}')
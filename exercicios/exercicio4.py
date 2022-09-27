"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido assim como as respetivas ilhas
- O maior valor inserido assim como as respetivas ilhas
- A média das vendas
"""

ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']

if __name__ == '__main__':
    vendas = []
    for ilha in ilhas:
        vendas.append((int(input(f'Insira as vendas para a ilhda da {ilha} '))))
    print(f'vendas={vendas}')

    menor = vendas[0]
    maior = vendas[0]
    for x in range(1, len(vendas)):
        if vendas[x] < menor:
            menor = vendas[x]
        if vendas[x] > maior:
            maior = vendas[x]
    print(f'O maior é {maior} e o menor é {menor}.')
    print(f'O maior é {max(vendas)} e o menor é {min(vendas)}.')
    print(f'O maior é {sorted(vendas)[4]} e o menor é {sorted(vendas)[0]}.')

    total = 0
    for v in vendas:
        total += v

    media = total / len(vendas)


    print(f'O total é {sum(vendas)} e a média é {media}.')
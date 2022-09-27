"""
Declare uma lista para guardar as vendas do grupo central feito
Declara uma lista para guardar os nomes das cinco ilhas do grupo central feito
Peça dados ao utilizador e guarde-os na lista feito
Após o utilizador ter inserido os 5 valores apresente: feito
- Total das vendas feito
- O menor valor inserido assim como as respetivas ilhas
- O maior valor inserido assim como as respetivas ilhas
- A média das vendas feito
"""
if __name__ == '__main__':
    #print(f'Incira 5 valores')

    ListadeVendas = []
    Tamanho = ListadeVendas.__len__()
    ListadeNomes = ['Terceira', 'Pico', 'Faial', 'São Jorge', 'Graciosa']

    for ilha in ListadeNomes:
        ListadeVendas.append((int(input(f'Insira as vendas para {ilha} '))))
    print(f'vendas={ListadeVendas}')

    soma = sum(ListadeVendas)
    minimo = min(ListadeVendas)
    maximo = max(ListadeVendas)
    total = 0
    for v in ListadeVendas:
        total += v

    media = total / len(ListadeVendas)

    print(f'Total da soma é {soma}')
    print(f'A venda mais alta é {maximo} e vem da ilha {ListadeNomes}')
    print(f'A venda mais baixa foi {minimo} e vem da ilha {ListadeNomes}')
    print(f'A media é de {media}')
    print(f'A lista de vendas é {ListadeVendas}')

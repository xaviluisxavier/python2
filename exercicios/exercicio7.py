"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha
Exemplo da estrutura de armazenamento das vendas:
    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]
    ou então:
    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]
"""

if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55]
    ]
    print(vendas)

    for venda in vendas:  # imprime as duas listas
        print(venda)
        for v in venda:  # imprime os valores da lista
            print(v)

    x = 0
    y = 3

    print(f'vendas[x][y] = {vendas[x][y]}')  # mostra as celulas x e y

    for x in range(2):  # 0, 1
        for y in range(5):  # 0, 1, 2, 3, 4
            print(f'vendas[{x}][{y}] = {vendas[x][y]}')  # mostra as celulas x e y

    print()
    for x in range(len(vendas)):
        for y in range(len(vendas[0])):
            print(f'vendas[{x}][{y}] = {vendas[x][y]}')  # mostra as celulas x e y

    # total de vendas

    total_vendas = 0
    for x in range(2):  # 0, 1
        total_linha = 0
        for y in range(5):  # 0, 1, 2, 3, 4
            # print(f'vendas[{x}][{y}] = {vendas[x][y]}')  # mostra as celulas x e y
            total_vendas = total_vendas + vendas[x][y]  # total das vendas
            total_linha = total_linha + vendas[x][y]  # total de cada linha
        print(f'total_linha = {total_linha}')
    print(f'total_vendas = {total_vendas}')

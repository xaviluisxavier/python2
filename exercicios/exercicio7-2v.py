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
vendas = [
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55]
]

if __name__ == '__main__':

    soma = 0
    total = 0
    for y in range(5):
        for x in range(2):
            soma += vendas[x][y]
            print(f'x = {x} y = {y}')

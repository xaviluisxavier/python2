"""
Pedir ao utilizador BI, Nome, Morada, Codigo Postal, Salario, custo hora, ano nascimento
"""

"""
inf = {
    'BI': 0,
    'NOME': '',
    'MORADA': '',
    'CODIGO-POSTAL': '',
    'ANO-NASCIMENTO': '',
    'SALARIO': '',
    'CUSTO-HORA': ''

}

if __name__ == '__main__':

    for i in inf:
        inf[i] = input(f' Insira {i}: ')

    print(inf)

"""

pessoa = (1, 'Maria', {'morada': 'Rua de Cima, 1', 'cp': 9500}, 12.50, [123, 435, 234, 3322.3])

meses = {'janeiro', 'fevereiro','março'}


if __name__ == '__main__':

    """
    print(pessoa[2].keys())
    print(pessoa[2].values())
    print()
    for k in pessoa[2].keys():
        print(k)
    print()
    for v in pessoa[2].values():
        print(v)
    print()
    for k in pessoa[2].keys():
        print(f'{k} = {pessoa[2][k]}')
"""
    meses.add('Abril')
    print(meses)
    meses.pop()
    print(meses)
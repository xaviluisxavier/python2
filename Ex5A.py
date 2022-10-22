"""
Pretende-se com este programa recolher informações acerda dos funcionários de uma empresa. Altere e complete o programa
tendo em atenção os seguintes objetivos.

Pergunte quantos funcionários a empresa tem e depois recolha os dados relativos a esse número de funcionários.
Após recolher toda a informção imprima:
O total de salários da empresa
O salário menor
O salário maior
A média de salários
O(s) nomes de quem ganha menos
(Os) nomes de quam ganha mais

ALtere o programa de forma a atingir os objetivos. É obrigatório usar o dicionário funcionário.
"""

funcionario = {'ID Funcionário': 0, 'Nome': '', 'Salário': 0.0}

if __name__ == '__main__':
    while True:
        funcionarios = []
        while True:
            for k in funcionario.keys():
                funcionario[k] = input(f'{k}? ')
            funcionarios.append(funcionario.copy())
            if input('Continuar? ') != 's':
                break
        for funcionario in funcionarios:
            print(funcionario)
        if input('Correr de novo [s/n]? ') != 's':
            break

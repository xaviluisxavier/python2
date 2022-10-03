"""
7. Escreva um programa em Python que lê o número de horas, que um em-
pregado trabalhou numa dada semana e o seu salário/hora e calcula o

ordenado semanal tendo em conta as horas extraordinárias. O salário é
calculado do seguinte modo: se o número de horas fôr menor que 40 então
salário é dado pelo produto do número de horas pelo salário hora, em caso
contrário recebe horas extraordinárias as quais são pagas a dobrar.
"""


def salario(valor1, valor2):
    if hora_semanal > 40:
        valor2 *= 2

    salario_semanal = valor1 * valor2

    return salario_semanal


if __name__ == '__main__':
    hora_semanal = int(input('Quantas horas trabalhou esta semana? '))
    salario_hora = int(input('Qual é o seu salário por hora? '))

    print(f'O seu salário é {salario(hora_semanal, salario_hora)}€.')

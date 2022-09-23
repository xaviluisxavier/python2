def notas(valor):
    i = "erro"

    if valor >= 0:
        i = "E"
    if valor >= 20:
        i = "D"
    if valor >= 40:
        i = "C"
    if valor >= 60:
        i = "B"
    if valor >= 80:
        i = "A"
    if valor >= 100:
        i = "Erro"

    return i


if __name__ == '__main__':
    nome = input("Como te chamas? ")
    while True:
        fator = float(input("Insira a sua nota: "))
        print(f' {nome}, A tua nota é:  {notas(fator)}')
        continuar = input('repetir [s | n]? ')
        if continuar == 'n':
            break
print(f'adeus {nome}!')

"""
2. Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em Km) e o tempo necessário para a percorrer (em
minutos), e calcula a velocidade média em:
(a) Km / h
(b) m/s
"""


def media_km(valor1, valor2):
    valor1 = valor2 / 1000
    media = valor1 / valor2

    return media


def media_m(valor1, valor2):
    valor1 = valor2 / 1000
    valor2 = valor2 * 60
    media = valor1 / valor2

    return media


if __name__ == "__main__":
    distancia = int(input("Distancia percorrida em km: "))
    tempo = int(input("Tempo para percorrer em minutos:  "))

    print(f'{distancia}(Km) : {tempo}(min) = {media_km(distancia, tempo)} km/h')
    print(f'{distancia}(Km) : {tempo}(min) = {media_m(distancia, tempo)} m/s')

    print(f"A velocidade média é: {tempo} km/h")


if __name__ == '__main__':
    list_caracteres = ['.', '!', '?']
    frase = ''
    x = 0

    while x < 10:
        frase = str(input('Digite uma frase com mais de 10 caracteres: '))
        x = len(frase)
        y = x - 1
        if x < 10:
            print('A frase tem que ter mais de 10 caracteres.')

        elif frase[y] in list_caracteres:
            print('', end='')
        else:
            print('A frase tem que terminar com um deste pontos ".", "!", "?".')
            x = 0

        caracteres = frase[0]
        for a in range(1, len(frase)):
            if caracteres == frase[a]:
                print('A frase não pode conter mais de dois carecteres iguais de seguinda.')
                x = 0
                break
            caracteres = frase[a]

    print(frase)
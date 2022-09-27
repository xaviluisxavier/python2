"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Imprima a frase, mas com cada palavra invertida. Por exemplo 'Bom dia!' deve dar 'moB !aid'
 - Imprima a frase, mas com as maiusculas em minisculo e as minusculas em maiusculas.
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""

if __name__ == '__main__':

    frase = ''
    palavras = ''
    num_vogais = 0
    maiusculas = 0
    minusculas = 0
    numeros = 0

    try:
        frase = input('Insira frase: ')
    except TypeError:
        print('Frase inválida')

    palavras = frase.split(' ')

    frase_palavras_invert = ''
    for c in palavras:
        frase_palavras_invert += c[::-1] + ' '

    vogais = 'aeiou'
    frase_mM_inv = ''
    for char in frase:
        if char in vogais:
            num_vogais += 1
        if char.isalpha() and char != ' ':
            if char.islower():
                minusculas += 1
                frase_mM_inv += char.upper()
            else:
                maiusculas += 1
                frase_mM_inv += char.lower()
        elif char.isalnum():
            numeros += 1
        elif char == ' ':
            frase_mM_inv += char

    print(frase_palavras_invert)
    print(frase_mM_inv)
    print(f'Palavras: {len(palavras)}')
    print(f'Vogais: {num_vogais}')
    print(f'Maiusculas: {maiusculas}')
    print(f'Minusculas: {minusculas}')
    print(f'Números: {numeros}')
    frase = frase[::-1]
    print(frase)
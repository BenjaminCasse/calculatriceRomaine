def chiffreRomainToBase10(chiffreRomain):
    if type(chiffreRomain) is str:
        chiffreRomain = chiffreRomain.upper()
        conversionChiffresRomain = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        somme = 0
        for indiceChiffreRomain in range(len(chiffreRomain)):
            valeur = conversionChiffresRomain[chiffreRomain[indiceChiffreRomain]]
            if (indiceChiffreRomain + 1 < len(chiffreRomain)) and (
                    conversionChiffresRomain[chiffreRomain[indiceChiffreRomain + 1]] > valeur):
                somme -= valeur
            else:
                somme += valeur
    else:
        return "ERROR_INVALID_INPUT_TYPE"
    return somme


def base10ToChiffreRomain(chiffreRomain):
    chiffresBase10 = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    chiffresRomain = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    resultat = []
    for i in range(len(chiffresBase10)):
        occurence = int(chiffreRomain / chiffresBase10[i])
        resultat.append(chiffresRomain[i] * occurence)
        chiffreRomain -= chiffresBase10[i] * occurence
    return ''.join(resultat)


def calculatriceChiffreRomain(chiffreRomain1, operateur, chiffreRomain2):
    if operateur == '+':
        return chiffreRomainToBase10(chiffreRomain1) + chiffreRomainToBase10(chiffreRomain2)
    elif operateur == '-':
        return chiffreRomainToBase10(chiffreRomain1) - chiffreRomainToBase10(chiffreRomain2)
    elif operateur == '/':
        if chiffreRomain2 == 0:
            return "ERROR_DIVISION_BY_ZERO"
        else:
            return int(chiffreRomainToBase10(chiffreRomain1) / chiffreRomainToBase10(chiffreRomain2))
    elif operateur == '*':
        return chiffreRomainToBase10(chiffreRomain1) * chiffreRomainToBase10(chiffreRomain2)
    else:
        return "ERROR_INVALID_OPERATOR"


def calculatriceChiffreRomainBonus(chiffreRomain1, operateur, chiffreRomain2):
    if operateur == '+':
        return base10ToChiffreRomain(chiffreRomainToBase10(chiffreRomain1) + chiffreRomainToBase10(chiffreRomain2))
    elif operateur == '-':
        return base10ToChiffreRomain(chiffreRomainToBase10(chiffreRomain1) - chiffreRomainToBase10(chiffreRomain2))
    elif operateur == '/':
        if chiffreRomain2 == 0:
            return "ERROR_DIVISION_BY_ZERO"
        else:
            return base10ToChiffreRomain(
                int(chiffreRomainToBase10(chiffreRomain1) / chiffreRomainToBase10(chiffreRomain2)))
    elif operateur == '*':
        return base10ToChiffreRomain(chiffreRomainToBase10(chiffreRomain1) * chiffreRomainToBase10(chiffreRomain2))
    else:
        return "ERROR_INVALID_OPERATOR"

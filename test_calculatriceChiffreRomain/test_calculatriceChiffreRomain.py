import calculatriceChiffreRomain.calculatriceChiffreRomain as calc

def test_chiffreRomainToBase10():
    assert calc.chiffreRomainToBase10('I') == 1
    assert calc.chiffreRomainToBase10('V') == 5
    assert calc.chiffreRomainToBase10('X') == 10
    assert calc.chiffreRomainToBase10('L') == 50
    assert calc.chiffreRomainToBase10('C') == 100
    assert calc.chiffreRomainToBase10('D') == 500
    assert calc.chiffreRomainToBase10('M') == 1000
    assert calc.chiffreRomainToBase10("IV") == 4
    assert calc.chiffreRomainToBase10("VI") == 6
    assert calc.chiffreRomainToBase10(6) == "ERROR_INVALID_INPUT_TYPE"

def test_calculatriceChiffreRomain():
    assert calc.calculatriceChiffreRomain('M', '+', 'M') == 2000
    assert calc.calculatriceChiffreRomain('M', '-', 'C') == 900
    assert calc.calculatriceChiffreRomain('X', '*', 'X') == 100
    assert calc.calculatriceChiffreRomain('M', '/', 'M') == 1
    assert calc.calculatriceChiffreRomain('M', '^', 'M') == "ERROR_INVALID_OPERATOR"

def test_calculatriceChiffreRomainBonus():
    assert calc.calculatriceChiffreRomainBonus('M', '+', 'M') == "MM"
    assert calc.calculatriceChiffreRomainBonus('M', '-', 'C') == "CM"
    assert calc.calculatriceChiffreRomainBonus('X', '*', 'X') == 'C'
    assert calc.calculatriceChiffreRomainBonus('M', '/', 'M') == 'I'
    assert calc.calculatriceChiffreRomainBonus('M', '^', 'M') == "ERROR_INVALID_OPERATOR"


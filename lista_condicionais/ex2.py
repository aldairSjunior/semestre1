while True:
    valores = input('\nDigite os valores dos coeficientes para formular uma equação de 2º grau: ').split()
    val = [int(x) for x in valores]

    a = val[0]
    b = val[1]
    c = val[2]

    if a == 0:
        print('\nA não pode ser igual a 0')
        continue

    eq = b**2 - 4*a*c

    if eq > 0:
        print('\nExistem 2 raízes reais distintas nessa equação')

    elif eq < 0:
        print('\nExistem 2 raízes imaginárias conjugadas nessa equação')

    else:
        print('\nExistem 2 raízes reais iguais nessa equação')
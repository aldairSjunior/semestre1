while True:
    h = float(input('\nInforme sua altura (ex.: 1.80): '))
    s = input('\nInforme seu sexo (M ou m, F ou f): ')

    if s == 'm' or s == 'M':
        cal = (72.7 * h) - 58
        print(f'\nSeu peso ideal é {cal}kg')
    
    elif s == 'f' or s == 'F':
        cal = (62.1 * h) - 44.7
        print(f'\nSeu peso ideal é {cal}kg')

    else:
        print('\nSexo inválido!')

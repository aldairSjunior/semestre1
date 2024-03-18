while True:
    nota = float(input('\nInforme sua nota: '))

    if nota >= 7:
        print('\nEstudante aprovado!')

    if nota < 4:
        print('\nEstudante em recuperação!')

    else:
        print('\nEstudante reprovado!')
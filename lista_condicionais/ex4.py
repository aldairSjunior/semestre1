while True:
    nota = float(input('\nInforme sua nota: '))

    if nota > 7:
        print('\nEstudante aprovado!')

    elif 4 <= nota <= 7:
        print('\nEstudante em recuperação!')

    else:
        print('\nEstudante reprovado!')
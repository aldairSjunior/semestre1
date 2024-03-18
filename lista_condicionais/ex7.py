while True:
    id = int(input('\nInforme sua idade: '))
    peso = float(input('\nInforme seu peso: '))

    if id > 15 and peso < 120:
        print('\nVocê está liberado!')
    
    else:
        print('\nVocê não está liberado!')


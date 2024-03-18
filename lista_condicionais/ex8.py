while True:
    id = int(input('\nInforme sua idade: '))

    if id < 16:
        print('\nVocê não é eleitor!')
    
    elif 16 <= id < 18 or id > 65:
        print('\nVocê é eleitor facultativo!')
    
    elif 18<= id <= 65:
        print('\nVocê é eleitor obrigatório!')
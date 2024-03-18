while True:
    temp = float(input('\nInforme a temperatura de hoje (em °C): '))

    if temp < 15:
        print('\nEstá frio!')

    elif temp > 25:
        print('\nEstá calor!')

    else:
        print('\nTemperatura agradável!')
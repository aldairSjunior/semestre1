while True:
    id = int(input('\nInforme sua idade: '))
    ts = int(input('\nInforme o tempo de serviço (em anos): '))

    if id >= 65 or ts >= 30 or id >= 60 and ts >= 25:
        print('\nEssa pessoa pode se aposentar!')

    else:
        print('\nEssa pessoa não pode se aposentar!')
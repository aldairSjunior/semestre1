p = []
i = []

while True:
    n = int(input('\nDigite um número inteiro: '))

    if n % 2 == 0:
        p.append(n)

    else:
        i.append(n)
    
    print('\nNúmeros pares: ',p)
    print('\nNúmeros ímpares: ',i)
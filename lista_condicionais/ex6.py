p = []
i = []

while True:
    n = int(input('\nDigite um número inteiro: '))

    if n % 2 == 0:
        p.append(n)

    else:
        i.append(n)
    
    print(f'\nNúmeros pares: ',p)
    print(f'\nNúmeros ímpares: ',i)
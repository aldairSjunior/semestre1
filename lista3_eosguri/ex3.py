p = []
i = []

while len(p) < 5 and sum(i) < 30:
    x = int(input('\nDigite um número inteiro: '))

    if x < 0:
        print('Número inválido! Digite um número positivo.')
        continue

    if x % 2 == 0:
        p.append(x)
        print(f'O número {x} é par!')

    else:
        i.append(x)
        print(f'O número {x} é ímpar!')

print(f'\nO número de pares digitados foi {len(p)}, que somados totalizam {sum(p)}')
print(f'\nO número de ímpares digitados foi {len(i)}, que somados totalizam {sum(i)}')
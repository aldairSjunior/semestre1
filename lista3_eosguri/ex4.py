n = int(input('Informe o número de elementos a ser digitado: '))
x = 0
numeros = []

while x < n:
    num = int(input(f'\nDigite o {x+1}º número: '))

    if num <= 10:
        print('Número inválido! Digite um número maior que 10.')
        continue
    numeros.append(num)

    x += 1

print(numeros)

soma = 0
cont = 0

while cont < 10:
    nota = float(input(f'Digite a {cont+1}ª nota: '))

    soma += nota
    cont += 1

media = soma/cont
print(f'\nA média foi de {media} pontos')
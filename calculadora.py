print('---CALCULADORA---\n')

while True:
    op = int(input('\nEscolha a operação: \n1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão \n5 - sair \n> '))

    if op == 5:
        print('\nObrigado por utilizar!')
        break

    elif op < 0 or op > 5:
        print('\nOpção inválida, tente novamente!')
        continue
    
    else:
        num = input('\nDigite 2 números para realizar a operação: ').split()
        numeros = [int(x) for x in num]

        if op == 1:
            print(f'\nA operação foi soma: {numeros[0]} + {numeros[1]} = {sum(numeros)}')

        elif op == 2:
            print(f'\nA operação foi subtração: {numeros[0]} - {numeros[1]} = {numeros[0] - numeros[1]}')

        elif op == 3:
            print(f'\nA operação foi multiplicação: {numeros[0]} * {numeros[1]} = {numeros[0] * numeros[1]}')

        elif op == 4:
            print(f'\nA operação foi divisão: {numeros[0]} / {numeros[1]} = {numeros[0] / numeros[1]}')






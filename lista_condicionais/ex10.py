while True:
    cod = int(input('Informe o código da sua universidade: '))
    n1 = float(input('Informe sua primeria nota do bimestre: '))
    n2 = float(input('Informe sua segunda nota do bimestre: '))
    media = (n1+n2)/2

    if cod == 1:
        if media >= 7:
            print('\nAluno aprovado!')

        elif 4 <= media < 7:
            print('\nAluno em exame!')

        else:
            ('\nAluno reprovado!')

    elif cod == 2:
        if media >= 5:
            print('Aluno aprovado!')

        else:
            print('\nAluno Em exame!')

    else:
        print('\nCódigo inválido!')
        continue
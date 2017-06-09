# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) - 44.7 (h = altura)
# c) Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

x = 1

# Enquanto x = 1
while(x == 1):

    #Dados do usuario
    altura = float(input('Quanto mede em Metros? '))
    peso = float(input('Quanto pesa em Kg?'))
    sexo = input('Qual seu sexo?[F/M] ').lower()



    if(sexo == 'f' or sexo == 'm'):
        # calcular o peso ideal
        if (sexo == 'f'):
            pesoIdeal = (72.7 * altura) - 58
        elif (sexo == 'm'):
            pesoIdeal = (62.1 * altura) - 44.7

        # imprime  o resultado
        if (peso > pesoIdeal):
            print('Voce está acima do peso ideal, deveria pesar {:.2f}'.format(pesoIdeal))
        elif (peso < pesoIdeal):
            print('VOce está abaixo do peso ideal, deveria pesar {:.2f}'.format(pesoIdeal))
        else:
            print('Voce tem o peso ideal! Parabéns')
            print('O seu peso ideal é {:.2f}'.format(pesoIdeal))
    else:
        print('Dados inválidos!')

    op = input("Clique \'Enter\' para continuar ou digite \'s\' para sair:\n ").lower()
    if (op == 's'):
        x = 0
        print("Obrigado e volte sempre... :-p")
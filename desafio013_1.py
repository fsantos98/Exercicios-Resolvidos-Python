# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com a percentagem que o funcionário
# quer de aumento!

print('{:=^35}'.format(' Desafio #012_1 '))

sair = False

while(sair == False):
    salario = float(input('Digite o seu salário: '))
    aumento = float(input('Digite o aumento desejado: '))

    salarioFinal = salario + ((salario * aumento) / 100)

    print('O seu salario que antes era {} é agora de {} ({}% de aumento)'.format(salario, salarioFinal, aumento))

    x = input('Deseja repetir o processo? [s/n]')
    if(x == 's'):
        sair = False
        print('Reiniciando o programa...')
    else:
        print('Encerrando o programa ... \n')
        sair = True
else:
    print('Programa encerrado!')
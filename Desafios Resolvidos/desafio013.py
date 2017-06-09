# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento!

print('{:=^35}'.format(' Desafio #013 '))

salario = float(input('Digite o seu salario: '))

salarioFinal = salario + ((salario * 15) / 100)

print('O seu salario que antes era {:.2f}€, é agora de {:.2f}€'.format(salario, salarioFinal))
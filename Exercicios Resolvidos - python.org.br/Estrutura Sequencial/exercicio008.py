# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganhosHora = float(input('Quanto ganha por hora? '))
horasTrabalhadasMes = float(input('Quantas horas trabalha por mês? '))

salarioMes = ganhosHora * horasTrabalhadasMes

print('Você trabalha {:.0f} horas por mes, ganhando {:.2f} por hora, fazendo um total de {:.2f} por mes!'.format(horasTrabalhadasMes, ganhosHora, salarioMes))

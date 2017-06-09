# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

while True:
    try:
        ganhosHora = float(input('Quanto ganha por hora? '))
        horasMes = int(input('Quantas horas trabalha por mes? '))
        salarioMes = ganhosHora * horasMes
        impostoRenda = (salarioMes * 11) / 100
        impostoINSS = (salarioMes * 8) / 100
        impostoSindicado = (salarioMes * 5) /100
        impostoTotal = impostoRenda + impostoINSS + impostoSindicado
        salarioLiquido = salarioMes - impostoTotal

    except Exception as erro:
        print('Erro: {}'.format(erro))

    else:
        print('\nO seu salario é de {:.1f}€'.format(salarioMes))
        print('Estão a ser retirados {:.1f}€ de imposto ao seu salário'.format(impostoTotal))
        print('Imposto Renda: {:.1f}€'.format(impostoRenda))
        print('Imposto INSS: {:.1f}€'.format(impostoINSS))
        print('Imposto Sindicado: {:.1f}€'.format(impostoSindicado))
        print('O seu salario liquido é de {:.1f}€'.format(salarioLiquido), end='\n\n')

    run = input('Deseja repetir o programa?[s/n]').lower()
    if(run != 's'):
        break
    else:
        pass
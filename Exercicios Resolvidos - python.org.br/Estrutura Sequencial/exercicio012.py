# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a
# seguinte fórmula: (72.7*altura) - 58

alturaCM = float(input('Qual a sua altura em CM? '))
alturaM = alturaCM / 100

pesoIdeal = (72.7*alturaM) - 58

print('O seu peso ideal é {:.1f}'.format(pesoIdeal))
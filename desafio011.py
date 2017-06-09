# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro pinta uma área de 2 metros quadrados!

print('{:=^35}'.format(' Desafio #011 '))

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura * altura
tintaNecessaria = area/2

print('A parede de medidas {:.2f}x{:.2f}m tem {:.2f}m de área '.format(largura, altura, area), end='')
print(' e são precisos {:.2f} litros de tinta para a pintar!'.format(tintaNecessaria))


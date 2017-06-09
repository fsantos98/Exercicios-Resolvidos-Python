# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# pi x raio^2
import math

raio = float(input('Raio (m): '))
area = math.pi * raio**2

print('Raio: {}m'.format(raio))
print('Área: {:.2f}m'.format(area))


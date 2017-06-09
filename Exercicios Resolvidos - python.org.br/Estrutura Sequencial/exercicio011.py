# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

a = (2 * n1) + (0.5 * n2)
b = (3 * n1) + n3
c = n3 ** 3

print('Operação a = {:.1f}'.format(a))
print('Operação b = {:.1f}'.format(b))
print('Operação c = {:.1f}'.format(c))

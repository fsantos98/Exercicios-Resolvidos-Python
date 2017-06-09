# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada!

numero = int(input('Digite um número: '))

print('O dobro de {} é: {},'.format(numero, numero * 2), end='\n')
print('o triplo de {} é {},'.format(numero, numero * 3), end='\n')
print('a raiz quadrada de {} é {:.2f}'.format(numero, numero**0.5))
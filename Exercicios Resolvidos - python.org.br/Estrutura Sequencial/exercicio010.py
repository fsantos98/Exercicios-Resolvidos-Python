# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temperaturaC = float(input('Temperatura em Celsius: '))
temperaturaF = (temperaturaC * 9/5 + 32)

print('Temperatura em Celsius: {:.1f}'.format(temperaturaC))
print('Temperatura em Farenheit: {:.1f}'.format(temperaturaF))
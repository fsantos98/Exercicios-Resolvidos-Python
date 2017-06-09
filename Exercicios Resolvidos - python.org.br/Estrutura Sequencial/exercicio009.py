# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

temperaturaF = float(input('Temperatura em farenheit: '))

temperaturaG = (5 * (temperaturaF-32) / 9)

print('Temperatura em farenheit: {}'.format(temperaturaF))
print('Temperatura em graus: {:.1f}'.format(temperaturaG))
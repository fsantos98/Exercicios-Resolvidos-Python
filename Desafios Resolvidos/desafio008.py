# Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros!

valor = float(input('Digite um valor em metros para ser convertido: '))

centimetros = int(valor * 100)
milimetros = int(valor * 1000)

print('{:.0f}m equivale a {}cm e {}ml'.format(valor, centimetros, milimetros))
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# 1$ = R$3.27

print('{:=^35}'.format(' Desafio #010 '))

dinheiro = int(input('Quantos reais voce tem? '))
cotacaoReal = 3.27
dolares = int(dinheiro//cotacaoReal)

print('Pode comprar {} dolares com {} reais!'.format(dolares, dinheiro))
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto!

print('{:=^35}'.format(' Desafio #012 '))

preco = float(input('Quanto custa? '))

precoFinal = preco - ((preco * 5) / 100)

print('O seu produto que antes custava {:.2f}, com 5% de desconto, custa agora {:.2f}'.format(preco, precoFinal))
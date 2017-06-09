# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com o desconto que o usuario quiser de desconto!

print('{:=^36}'.format(' Desafio #012_1 '))

sair = False

while(sair == False):
    preco = float(input('Digite o preço de um produto: '))
    desconto = float(input('Digite o desconto que quer: '))
    precoFinal = preco - ((preco * desconto) / 100)

    print('O produto que antes custava {:.2f}€, com {:.2f}% desconto, custa agora {:.2f}€ \n\n'.format(preco, desconto, precoFinal))

    x = input('Deseja repetir?[s/n]').lower()
    if(x == 's'):
        sair = False
        print('Reiniciando programa... \n\n')
    else:
        sair = True
        print('Encerrando programa... \n\n')

else:
    print('Programa encerrado!')


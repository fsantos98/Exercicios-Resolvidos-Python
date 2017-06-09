# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 08 '))

while True:
    try:
        nome1 = input('Qual o produto 1? ')
        preco1 = float(input('Qual o preço do produto 1? '))
        nome2 = input('Qual o produto 2? ')
        preco2 = float(input('Qual o preço do produto 2? '))
        nome3 = input('Qual o produto 3? ')
        preco3 = float(input('Qual o preço do produto 3? '))

    except Exception as erro:
        print({'Erro: {}'}.format(erro))
    else:

        if(preco1 < preco2):
            if(preco1 < preco3):
                print('Tem de comprar o produto {} que custa {:.2f}€'.format(nome1, preco1))
        else:
            if(preco2 < preco3):
                print('Tem de comprar o produto {} que custa {:.2f}€'.format(nome2, preco2))
            else:
                print('Tem de comprar o produto {} que custa {:.2f}€'.format(nome3, preco3))


    stop = input('Deseja reiniciar o programa?[s/n]')
    if(stop != 's'):
        break
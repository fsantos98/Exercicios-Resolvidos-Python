#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor.

print('{:=^35}'.format(' Desafio 017 '))

while True:
    try:
        areaPintada = float(input('Digite o tamanho da área a ser pintada em metros quadrados: '))
        tintaNecessaria = areaPintada /6
        latasNecessarias = tintaNecessaria//18
        galoesNecessarios = tintaNecessaria//3.6

        if(latasNecessarias < 1):
            latasNecessarias = 1
        elif(latasNecessarias != tintaNecessaria/18):
            latasNecessarias += 1

        if(galoesNecessarios < 1):
            galoesNecessarios = 1
        elif(galoesNecessarios != tintaNecessaria/3.6):
            galoesNecessarios += 1

        precoLatas = latasNecessarias * 80
        precoGaloes = galoesNecessarios * 25

        if(tintaNecessaria <= 3.6):
            qntLatasNecessarias = 0
            qntGaloesNecessarios = 1
        elif(tintaNecessaria <= 18):
            qntLatasNecessarias = 1
            qntGaloesNecessarios = 0
        elif(tintaNecessaria >= 18):
            qntLatasNecessarias = tintaNecessaria//18
            tintaRestante = tintaNecessaria - (qntLatasNecessarias * 18)
            qntGaloesNecessarios = tintaRestante//3.6
            if(qntGaloesNecessarios != tintaRestante/3.6):
                qntGaloesNecessarios +=1

        precoLatasB = qntLatasNecessarias * 80
        precoGaloesB = qntGaloesNecessarios * 25
        totalLatasGaloes = precoGaloesB + precoLatasB

    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        print('Preço apenas com latas: {:.0f} latas - {}€'.format(latasNecessarias, precoLatas))
        print('Preço apenas com galões: {:.0f} galões - {}€'.format(galoesNecessarios, precoGaloes))
        print('\n\nPreço mais barato: ')
        print('Latas: {:.0f} - {:.2f}€'.format(qntLatasNecessarias, precoLatasB))
        print('Galoes: {:.0f} - {:.2f}€'.format(qntGaloesNecessarios, precoGaloesB))
        print('Total = {:.2f}€'.format(totalLatasGaloes))
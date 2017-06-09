# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print('{:=^35}'.format(' Exercicio 016 '))

while True:
    try:
        areaPintar = float(input('Quantos metros quadrados são necessários pintar? '))
        tintaNecessaria = areaPintar/3
        latasNecessarias = int(tintaNecessaria//18)
        if(latasNecessarias < 1):
            latasNecessarias = 1
            precoTotal = 80
        else:
            precoTotal = latasNecessarias * 80

    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        print('Quantidade de latas necessárias: {}'.format(latasNecessarias))
        print('Preço total:  {:.1f}€'.format(precoTotal))

    run = input('Deseja repetir?[s/n]')
    if(run != 's'):
        break

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 02 '))

while True:
    try:
        numero = float(input('Digite um número: '))
    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        if(numero >= 0):
            print('O número {:.1f} é positivo.'.format(numero))
        else:
            print('O número {:.1f} é negativo.'.format(numero))

    stop = input('Parar?[s/n]')
    if(stop == 's'):
        break
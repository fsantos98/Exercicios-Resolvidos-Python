# Faça um Programa que leia três números e mostre o maior deles.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 06 '))

while True:
    try:
        numero1 = float(input('Numero 1: '))
        numero2 = float(input('Numero 2: '))
        numero3 = float(input('Numero 3: '))

    except Exception as erro:
        print('Erro: {}'.format(erro))

    else:
        if(numero1 > numero2):
            if(numero1 > numero3):
                print('O maior número é: {:.2f}'.format(numero1))
            else:
                print('O maior número é: {:.2f}'.format(numero3))
        else:
            if(numero2 > numero3):
                print('O maior número é: {:.2f}'.format(numero2))
            else:
                print('O maior número é: {:.2f}'.format(numero3))

    stop = input('Deseja reiniciar?[s/n]')
    if(stop != 's'):
        break
# Faça um Programa que peça dois números e imprima o maior deles.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 01 '))

while True:
    try:
        numero1 = int(input('Digite um valor inteiro: '))
        numero2 = int(input('Digite outro valor inteiro: '))
    except Exception as erro:
        print({'Erro: {}'}.format(erro))
    else:
        if(numero1 > numero2):
            print(numero1)
        elif(numero2 > numero1):
            print(numero2)
        else:
            print('Ambos têm o mesmo valor: {} e {}'.format(numero1, numero2))

    stop = input('Deseja parar o programa?[s/n]')
    if(stop != 'n'):
        break
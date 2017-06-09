# Faça um Programa que leia três números e mostre-os em ordem decrescente.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 09 '))

while True:
    try:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        numero3 = int(input('Digite mais um número: '))

        if(numero1 > numero2 and numero2 > numero3):
            primeiro = numero1
            segundo = numero2
            terceiro = numero3
        elif(numero1 > numero2 and numero1 > numero3):
            primeiro = numero1
            segundo = numero3
            terceiro = numero2
        elif(numero3 > numero2 and numero2 > numero1):
            primeiro = numero3
            segundo = numero2
            terceiro = numero1
        elif(numero3 > numero1 and numero1 > numero2):
            primeiro = numero3
            segundo = numero1
            terceiro = numero2
        elif(numero2 > numero1 and numero1 > numero3):
            primeiro = numero2
            segundo = numero1
            terceiro = numero3
        elif(numero2 > numero3 and numero3 > numero1):
            primeiro = numero2
            segundo = numero3
            terceiro = numero1
        else:
            raise Exception('Algo deu errado! Todos os números devem ser diferentes!')

    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        print('Ordem: {} -> {} -> {}'.format(primeiro, segundo, terceiro))

    stop = input('Deseja reiniciar o programa?[s/n]')
    if(stop != 's'):
        break




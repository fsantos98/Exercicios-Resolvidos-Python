# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 04 '))

while True:
    try:
        letra = input('Insira uma letra: ')

        if(len(letra) > 1):
            raise Exception('Demasiadas letras!')

        if(letra == 'a' or letra == 'e' or letra == 'i' or letra == '0' or letra == 'u'):
            msg = 'Vogal'
        else:
            msg = 'Consoante'
    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        print('A letra \'{}\' é uma {}'.format(letra, msg))

    stop = input('Deseja reiniciar?[s/n]')
    if(stop != 's'):
        break

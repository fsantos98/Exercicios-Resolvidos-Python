# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 10 '))

while True:
    print('Em que turno você estuda?')
    print('M -> matutino')
    print('V -> Vespertino')
    print('N -> Noturno')
    try:
        resposta = input('Em que turno voce estuda? ').upper()

    except Exception as erro:
        print({'Erro: {}'}.format(erro))
    else:
        if(resposta == 'M'):
            print('Bom dia')
        elif(resposta == 'V'):
            print('Boa tarde')
        elif(resposta == 'N'):
            print('Boa noite')
        else:
            print('Valor inválido!')

    stop = input('Deseja reiniciar o programa?[s/n]')
    if(stop != 's'):
        break





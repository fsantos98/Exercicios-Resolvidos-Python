# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 05 '))

while True:
    try:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        media = (nota1+nota2)/2

        if(nota1 > 10 or nota2 > 10):
            raise Exception('Notas inseridas têm de estar entre 0 e 10')

        if(media >= 7 and media < 10):
            msg = 'Aprovado'
        elif(media < 7):
            msg = 'Reprovado'
        elif(media == 10):
            msg = 'Aprovado com Distinção'

    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        print('O aluno foi {} com média de {}'.format(msg, media))

    stop = input('Deseja reiniciar?[s/n]').lower()
    if(stop != 's'):
        break


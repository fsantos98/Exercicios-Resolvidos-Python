# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print('{:=^35}'.format(' Desafio 018 '))

while True:
    try:
        tamanhoMB = float(input('Quantos MB tem o seu arquivo? '))
        velocidadeInternetMB = float(input('Qual a sua velocidade(MBPS)? '))
        duracaoDownload = tamanhoMB/velocidadeInternetMB/60

    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        print('O seu arquivo de {:.0f}mb irá demorar {:.2f}minutos'.format(tamanhoMB, duracaoDownload))


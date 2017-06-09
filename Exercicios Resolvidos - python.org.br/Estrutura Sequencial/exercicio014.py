# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o
# valor da multa que João deverá pagar. Caso contrário mostrar tais
# variáveis com o conteúdo ZERO.

while True:
    try:
        pesoPeixe = float(input('Quanto pesa o peixe em KG? '))
    except:
        print('Dados inválidos!')
    else:
        if(pesoPeixe < 1):
            print('O peixe tem de pesar pelo menos 1 Kg!')
        elif(pesoPeixe > 50):
            excesso = int(pesoPeixe - 50)
            multa = int(excesso * 4)
            print('O peixe tem {:.2f}kg, logo tem {} a mais. Terá de pagar uma multa de {}R$'.format(pesoPeixe, excesso, multa))
        else:
            excesso, multa = 0, 0
            print('O peixe tem {:.2f}kg, logo não tem peso a mais nem multa!'.format(pesoPeixe))

    x = input(('Restart?[s/n]')).lower()
    if(x == 's'):
        pass
    else:
        break
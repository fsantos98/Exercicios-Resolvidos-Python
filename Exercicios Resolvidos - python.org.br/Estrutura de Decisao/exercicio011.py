# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
# o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 11 '))

while True:
    try:
        salario = float(input('Digite o valor do seu salario: '))

        if(salario >= 0 and salario <= 280):
            aumentoPerc = 20
            aumentoSalario = (salario * aumentoPerc) / 100
            salarioFinal = salario + aumentoSalario
        elif(salario > 280 and salario <= 700):
            aumentoPerc = 15
            aumentoSalario = (salario * aumentoPerc) / 100
            salarioFinal = salario + aumentoSalario
        elif(salario > 700 and salario  <= 1500):
            aumentoPerc = 10
            aumentoSalario = (salario * aumentoPerc) / 100
            salarioFinal = salario + aumentoSalario
        elif(salario > 1500):
            aumentoPerc = 5
            aumentoSalario = (salario * aumentoPerc) / 100
            salarioFinal = salario + aumentoSalario
        else:
            raise Exception('Salario não pode ser negativo!')

    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        print('Salario inicial: {:.2f}€'.format(salario))
        print('% aumentada: {:.2f}€'.format(aumentoPerc))
        print('Valor do aumento: {:.2f}€'.format(aumentoSalario))
        print('Novo salário: {:.2f}€'.format(salarioFinal))

    stop = input('Deseja reiniciar o programa?[s/n]')
    if(stop != 's'):
        break

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.

print('{:=^55}'.format(' Estrutura de Decisão - Desafio 03 '))

while True:
    try:
        sexo = input('Digite o seu sexo [M/F]: ').upper()
    except Exception as erro:
        print('Erro: {}'.format(erro))
    else:
        if(sexo == 'F'):
            print('Feminino')
        elif(sexo == 'M'):
            print('Masculino')
        else:
            print('Sexo inválido!')

    stop = input('Deseja reinciar?[s/n]').lower()
    if(stop != 's'):
        break
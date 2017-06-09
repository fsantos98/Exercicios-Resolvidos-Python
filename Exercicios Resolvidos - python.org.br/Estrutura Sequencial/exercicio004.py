# Faça um Programa que peça as 4 notas bimestrais e mostre a média

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('1ª nota-> {}\n2ª nota ->{}\n3º nota -> {}\n4ª nota -> {}'.format(nota1, nota2, nota3, nota4))
print('Média: {}'.format(media))
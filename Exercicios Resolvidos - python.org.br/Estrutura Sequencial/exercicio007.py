# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

ladoQuadrado = float(input('Quanto mede o lado do quadrado? '))

areaQuadrado = ladoQuadrado * ladoQuadrado
areaQuadrado2 = areaQuadrado * 2

print('Área do quadrado: {:.1f}'.format(areaQuadrado))
print('Dobro da área: {:.1f}'.format(areaQuadrado2))
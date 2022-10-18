# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

x = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(x, (x*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(x, (x*3), x, pow(x, (1/2))))

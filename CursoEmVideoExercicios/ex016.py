# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua posição inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
''' from math import trunc
numero = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, trunc(numero))) '''

numero = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(numero, int(numero)))

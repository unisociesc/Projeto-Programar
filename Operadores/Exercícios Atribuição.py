#Exercícios Operadores de Atribuição

# 1 - Faça um programa que some valores utilizando o operador de atribuição.

num1 = float(input('Digite um valor: '))

soma = float(input('\nDigite o valor que queira somar: '))

sub = float(input('\nDigite o valor que queira diminuir: '))

print('\nO valor antes da soma é', num1)

num1 += soma

print('\nO valor após a soma é', num1)

num1 -= sub

print('\nO valor após a subtração é', num1)

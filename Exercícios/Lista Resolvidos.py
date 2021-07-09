#1

print('Alo Mundo')

#2

numero = int(input('Informe um número: '))

print('Esse é o número informado',numero)

#3

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
teste = bool(input('Digite True caso goste de programar, ou False caso não goste: '))

print(nome)
print(idade)
print(altura)
print(teste)

#4

print('Soma de valores...\n')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

soma = num1 + num2


#%s = string 
#%d = inteiros
#%f = floats
#%g = genéricos


print('O resultado da soma de', num1,'+', num2,'é', soma)
print('O resultado da soma de %g + %g é %g' % (num1,num2,soma))

#5

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))

media = n1 + n2 + n3 + n4 / 4

print('A média do aluno foi %g' % media)

#6

metros = float(input('Digite o valor em metros que queira converter: '))

convertido = metros * 100

print('O valor convertido de %g metros para centímetros é %g cm' % (metros, convertido))

#7

print('Cálculo do peso ideal!\n')

altura = float(input('Informe sua altura: '))

homem = (72.7*altura) - 58
mulher = (62.1*altura) - 44.7

print('O peso ideal para homem é', homem,'e para mulher', mulher)

#8

num1 = float(input('Digite um valor: '))

soma = float(input('\nDigite o valor que queira somar: '))

sub = float(input('\nDigite o valor que queira diminuir: '))

print('\nO valor antes da soma é', num1)

num1 += soma

print('\nO valor após a soma é', num1)

num1 -= sub

print('\nO valor após a subtração é', num1)

#9

lado = float('Informe o tamanho da lateral do quadrado: ')

area = lado**2

dobro = area*2

print('A área do quadrado é', area)
print('O dobro dessa área é', dobro)

#Desafio


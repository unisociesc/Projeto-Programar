#Exercícios Operadores Aritméticos

# 1- Faça um Programa que peça dois números e imprima a soma.

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

# 2- Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))

media = n1 + n2 + n3 + n4 / 4

print('A média do aluno foi %g' % media)


# 3- Faça um Programa que converta metros para centímetros.

metros = float(input('Digite o valor em metros que queira converter: '))

convertido = metros * 100

print('O valor convertido de %g metros para centímetros é %g cm' % (metros, convertido))

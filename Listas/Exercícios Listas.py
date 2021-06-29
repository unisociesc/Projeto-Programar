#Exercícios - Listas

# 1- Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caract = []
vogais = ['a','e','i','o','u']

cont = 0
x = 1

while x <= 10:
  entrada = str(input('Caracter %d:'%x))
  x += 1
  caract.append(entrada)
  if (entrada in vogais):
    cont += 1

print(caract)

print('\n')

quant = 10 - cont

print('Consoantes:', quant)

# 2- Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
par = []
impar = []

for n in range(0,10):
  novo = int(input('Digite um número: '))
  while (novo < 0):
    novo = int(input('Digite um número válido: '))
  vetor.append(novo)

for n in range(0,10):
  if (vetor[n] % 2 == 0):
    par.append(vetor[n])
  else:
    impar.append(vetor[n])

print('Vetor com 10 elementos:', vetor)
print('Vetor com elementos pares:', par)
print('Vetor com elementos impares:', impar)

#Estrutura de Controle - if / Exercícios

#1- Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input('Digite um valor: '))

if (num>0):
  print('O número é positivo!')
else:
  print('O número é negativo')

#2- Faça um programa que verifique se uma letra digitada é F ou M. Conforme a letra escrever se é feminino ou masculino.

print('Digite M-Masculino ou F-Feminino\n')

letra = str(input('Qual é o sexo desta pessoa? '))

if (letra == 'M' or letra == 'm'):
  print('Masculino')
else:
  if (letra == 'F' or letra == 'f'):
    print('Feminino')
  else:
    print('Indefinido - Digite novamente')

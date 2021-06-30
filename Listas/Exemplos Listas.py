#Exercícios - Listas

# 1 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idade = []
altura = []

cont = 0
n = 3

for i in range(1,n+1):
  nova_idade = int(input('Digite a idade do %dº aluno: '%i))
  nova_altura = float(input('Digite a altura do %dº aluno: '%i))
  idade.append(nova_idade)
  altura.append(nova_altura)

soma_altura = sum(altura)

media_altura = soma_altura/len(altura)

for i in range(n):
  if (idade[i] > 13 and altura[i] < media_altura):
    cont += 1

print('\nO número de alunos que possuem mais de 13 anos e menos de', media_altura,'de altura são', cont)

# 2- Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

mes = ['Janeiro','Fevereiro', 'Março', 'Abril']
temp = []
menor = []

n = len(mes)

for i in range(n):
  print('Digite a temperatura do mês', mes[i])
  nova_temp = float(input())
  temp.append(nova_temp)

soma = sum(temp)

media = soma/n

print('\n')

for i in range(n):
  if (temp[i] < media):
    print('A temperatura do mês de',mes[i],'foi menor que a média de %g º'%media)
    menor.append(mes[i])

print('\n')

print('Os meses que tiveram a temperatura média menor que %gº C foram: '%media + str(menor))

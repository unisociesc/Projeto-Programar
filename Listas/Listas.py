# Listas

nomes = ['Matheus', 'Thiago'] # Para criar uma lista com elementos deve-se usar colchetes e adicionar os itens entre eles separados por vírgula.

nomes[0] = 'Ricardo' #As listas em Python são mutáveis, podendo ser alteradas depois de criadas. Para alterar um valor, é necessário checar o indice.

print(nomes) = ['Ricardo', 'Thiago']

nomes.append('Gustavo') #Com o método append() é possível adicionar itens na lista.

print(nomes) = ['Ricardo', 'Thiago', 'Gustavo'] #Sempre será adicionado na última posição.

nomes.insert(1, 'Lucas') #Com o método insert() é possível adicionar itens na lista e escolher a posição.

print(nomes) = ['Ricardo', 'Lucas' ,'Thiago', 'Gustavo']

nomes.remove('Gustavo') #Com o método remove() é possível remover itens na lista através do elemento informado.

print(nomes) = ['Ricardo', 'Lucas' ,'Thiago']

nomes.pop(1) #Com o método pop() é possível remover itens na lista pelo índice.

print(nomes) = ['Lucas' ,'Thiago']

#Primeiro Exemplo

vetor = []
n = int(5)

for i in range(n):
  print('Digite o valor do index', i)
  novo_valor = float(input())
  vetor.append(novo_valor)

print('\nEstes foram os valores salvos\n')

print(vetor)

vetor.reverse()

print(vetor)

# Segundo Exemplo

print('Verificação da média dos alunos!\n')

notas = []
n = int(input('Qual a quantidade de notas? '))

for i in range(1,n+1):
  print('Digite a nota', i)
  nova_nota = float(input())
  notas.append(nova_nota)

print(notas)

soma = sum(notas)

media = soma/n

print('\nEstá é a média do aluno:', media)

#Exercícios

# 1- Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# 2- Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

#Estrutura de Controle - if

idade = int(input('Digite a sua idade: '))#Recebe a idade

if (idade < 18): #Verifica se idade é menor que 18
  print('Menor de Idade')
else: #Se não for
  print('Maior de Idade')


#Teste de Notas

print('Verificação de rendimento dos alunos!\n')

print('Digite suas 3 notas:\n')

#Recebe as notas
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

soma = n1+n2+n3 #Soma as notas

if (soma<0 or soma>30): #Verifica se os valores estão corretos
  print('Somatório das notas divergentes, faça novamente....')
else: #Se estiverem corretos
  media = soma/3 #Cálculo da média
  condicao = None
  if (media == 10): #Se a média for 10
    condicao = 'Aprovado com mérito!!'
    print('A média do aluno foi', media, 'ele está', condicao)
  else:
    if (media>=7): #Se não for 10, mas é maior que 7
      condicao = 'Aprovado'
      print('A média do aluno foi', media, 'ele está', condicao)
    else: #Se for menor que 7
      condicao = 'Reprovado'
      print('A média do aluno foi', media, 'ele está', condicao)

#Estrutura de Controle - For 

print('Tabuada até 10\n')
mais = 'S'

while (mais == 'S' or mais == 's'):
  n = int(input('\nDigite o número que queira saber a tabuada: '))

  for i in range(1,11):
    resultado = n * i
    print(n,'X',i,'=',resultado)
  else:
    print('\nTabuada Finalizada')
    print('Gostaria de Fazer novamente? Digite "S"')
    mais = str(input())

print('Programa Finalizado')

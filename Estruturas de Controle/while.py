#Estrutura de Controle - While

contador = 1

while (contador <= 5):
  print(contador)
  contador += 1
  break

nota = float(input('Digite sua nota: '))

while (nota < 0 or nota > 10)
  nota = float(input('Digite uma nota entre 0 e 10: '))

print('Nota Válida!')  

""" Exercícios

1- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

3- Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 100;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).

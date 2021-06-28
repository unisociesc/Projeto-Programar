#Estrutura de Controle - While / Exercícios

"""1- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

nota = float(input('Insira uma nova de 0 até 10: '))

while(nota < 0 or nota > 10):
  nota = float(input('A nota deve ser entre 0 e 10!\nTente novamente: '))

print('Nota Válida!')

"""2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações"""

print('Digite um nome e senha\n')

nome = str(input('Nome: '))
senha = str(input('Senha: '))

while (nome == senha):
  print('A senha não pode ser igual ao usuário\nTente novamente.')
  nome = str(input('Nome: '))
  senha = str(input('Senha: '))

while (len(senha)<10):
  senha = str(input('A senha deve conter no mínimo 10 caracteres!\nTente novamente: '))

print('Dados gravados...')

"""3- Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 100;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres)."""

nome = str(input('Qual seu nome (Mínimo 4 caracteres): '))
idade = int(input('Sua idade: '))
salario = float(input('Salário: '))
sexo = str(input('Sexo ("F" para feminino ou "M" para masculino) '))
civil = str(input('Estado civil ("S" Solteiro, "C"  Casado, "V" Viuvo, "D" Divorciado) '))

while (len(nome) < 4):
  nome = str(input('Seu nome deve ter mais que 3 caracteres!\nDigite novamente: '))

while (idade < 0 or idade > 100):
  idade = int(input('Você deve ter entre 0 e 100 anos!\nDigite novamente: '))

while (salario < 0):
  salario = float(input('Sei que a coisa tá feia, mas não tem salário negativo!\nDigite novamente: '))

while (sexo != 'f' and sexo != 'F' and sexo != 'm' and sexo !='M'):
  sexo = str(input('Digite um valor válido, F-Feminino ou M-Masculino: '))

while (civil != 's' and civil != 'S') and (civil != 'C' and civil != 'c') and (civil != 'v' and civil != 'V') and (civil != 'd' and civil != 'D'):
  civil = str(input('Não tem estado civil, estranho...\nDigite novamente: '))

print('Dados Gravados!!')

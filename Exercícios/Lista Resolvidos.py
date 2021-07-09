#Variáveis e Operadores

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

qnt_ganha = float(input('Quanto ganha por hora? '))
horas_trabalhadas = int(input('Horas trabalhadas por mês: '))

salario_bruto = qnt_ganha * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print ('+ Salário Bruto : R$ %.2f' %salario_bruto)
print ('- IR: R$ %.2f' %ir )
print ('- INSS: R$ %.2f' %inss )
print ('- Sindicato: R$ %.2f' %sindicato )
print ('= Salário Liquido : R$ %.2f' %(salario_bruto - ir - inss - sindicato))

#Decisão

#1

n1 = input('Digite o primero numero: ')
n2 = input('Digite o segundo numero: ')

if n1 > n2:
    print n1,'é maior que',n2
elif n2 > n1:
    print n2,'é maior que',n1
else:
    print 'os numeros são iguais'
    
#2

n = int(input("Aqui vai o valor que o usuário irá digitar:"))

if(n < 0):
  print("O valor digitado é negativo!")
else:
  print("O valor digitado é positivo!")
  
#3

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro

if (segundo > maior):
  maior = segundo
if (terceiro > maior):
  maior = terceiro

print('Maior: ',maior)

#4

print('Digite M-Masculino ou F-Feminino\n')

letra = str(input('Qual é o sexo desta pessoa? '))

if (letra == 'M' or letra == 'm'):
  print('Masculino')
else:
  if (letra == 'F' or letra == 'f'):
    print('Feminino')
  else:
    print('Indefinido - Digite novamente')
    
#5

n1 = input('Digite sua nota: ')
n2 = input('Digite sua 2° nota: ')

nota = (n1 + n2) / 2

if nota >= 7 and nota < 10:     
    print 'Você foi Aprovado!!' 
elif nota >= 10:
    print 'Você foi Aprovado com Distinção!!'
else:
    print 'Infelizmente você foi reprovado'
    
#6

numero = int(input('Digite um numero inteiro positivo: '))

# Extraindo a unidade
unidade = numero % 10

# Eliminando a unidade de nosso número
numero = (numero - unidade)/10

# Extraindo a dezena
dezena = numero % 10

# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero

# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')

#7

numero = input('Digite um numero: ')

if numero == 1:
    print '1-Domingo'
elif numero == 2:
    print '2-Segunda'
elif numero == 3:
    print '3-Terça'
elif numero == 4:
    print '4-Quarta'
elif numero == 5:
    print '5-Quinta'
elif numero == 6:
    print '6-Sexta'
elif numero == 7:
    print '7-Sabádo'
else:
    print 'Intrada invalida'
    
#8

a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
# Testando se é triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
  print('Nao é um triangulo')
elif (a == b) and (a == c) :
  print('Equilatero')
elif (a==b) or (a==c) or (b==c):
  print('Isósceles')
else:
  print('Escaleno')
  
#9

#Uma das duas condições a seguir deve ser verdadeira:
#Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
#Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')
    
#Desafio

print("1- File Duplo\n2- Alcatra\n3- Picanha\n\n")
tipo = int(input("Digite o tipo: "))
quantidade = int(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartao Tabajara? 1p/ SIM - 2p/ NAO: "))

if tipo == 1:
  nome = "File Duplo"
if quantidade <= 5:
  preco = quantidade * 4.90
else:
  preco = quantidade * 5.80
        
if tipo == 2:
  nome = "Alcatra"
if quantidade <= 5:
  preco = quantidade * 5.90
else:
  preco = quantidade * 6.80

if tipo == 3:
  nome = "Picanha"
if quantidade <= 5:
  preco = quantidade * 6.90
else:
  preco = quantidade * 7.80

if resposta == 1:
  r = "SIM"
  desconto = ((preco * 5) /100)
  total = preco - desconto
else:
  r = "NAO"
  total = preco
    
print("\n***************************CUPOM FISCAL**************************************")
print("* Carne.......................................................... %s " %nome)
print("* Quantidade..................................................... %d KG " %quantidade)
print("* Preço......................................................... %2.f R$ " %preco)
print("* Cartao Tabajara................................................ %s " %r)
print("* Total com desconto............................................ %2.f R$ " %total)
print("******************************************************************************")

#Repetição - While

#1

nota=float(input("informe um numero de 0 a 10: "))

while (nota>10) or (nota<0):
    nota=float(input("informe um numero de 0 a 10: "))
    
#2

print("Faça já seu cadastro:")

usuario=str(input("usuário--> "))
senha=str(input("senha-->"))

while usuario==senha:
    print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("usuário--> "))
	senha=str(input("senha-->"))
else:
	print("Cadastro efetuado com sucesso!")
    
#3

#Nome: maior que 3 caracteres;

nome=str(input("informe um nome--> "))

while (len(nome) <=  3):
	nome=str(input("informe um nome--> "))

#Idade: entre 0 e 150;

idade=int(input("informe a idade--> "))

while (idade > 150 or idade < 0 :
	idade=int(input("informe a idade--> "))
	
	
#Salário: maior que zero;
       
salario=float(input("informe um salário--> "))
       
while (salario < 0):
	salario=float(input("informe um salário--> "))
	
#Sexo: 'f' ou 'm';

sexo=str(input("informe a inicial do seu sexo--> "))
       
while (sexo !="f" and sexo!="m"):
	sexo=str(input("informe a inicial do seu sexo--> "))
	
#Estado Civil: 's', 'c', 'v', 'd';

estado_civil=str(input("informe a inicial do seu estado civil-->"))
       
while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
	estado_civil=str(input("informe a inicial do seu estado civil-->"))

#4

popA = int(80000) 
popB = int(200000) 
anos = int(0)
cresA = float(0.03)
cresB = float(0.015)
       
while (popA < popB):
    anos += 1
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)
       
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % popA)
print("País B: %.0f" % popB)

#5

popA = float(input("informe a população da cidade A "))
popB = float(input("informe a população da cidade B "))
anos = 0
cresA = float(input("informe a taxa de crescimento da população da cidade A "))
cresB = float(input("informe a taxa de crescimento da população da cidade B "))
       
while popA < popB:
	popA+=round((popA*cresA)/100)
	popB+=round((popB*cresB)/100)
	anos=anos+1

print("levará",anos,"anos para população da cidade A ser maior que a cidade B")
print("populaçãoB-->",popB,"habitantes")

#6
       
num1 = float(input("digite o 1º numero--> "))
num2 = float(input("digite o 2º numero--> "))
num3 = float(input("digite o 3º numero--> "))
num4 = float(input("digite o 4º numero--> "))
num5 = float(input("digite o 5º numero--> "))
       
soma = num1+num2+num3+num4+num5
       
print("soma-->",soma,)
print("média-->",soma/5)
print("populaçãoA-->", popA,"habitantes")
    
#7
       
inicio = int(1)
fim = int(50)
       
while (inicio<=fim):
    if (inicio%2 != 0):
       print(inicio)
    inicio+=1
       
#8
       
n = int(input('Digite um número inteiro: '))
count = int(0)
i = int(0)

while (i <= n or count < 2):
  i += 1
  x = n % i
  if (x == 0):
    count += 1

if (count <= 2):
  print('É primo')
else:
  print('Não é primo')

#Repetição - For

#1
       
for i in range(1,11,1):
    print(i)
     
#2

n = int(input('Digite um número inteiro: '))

for i in range(1,11,1):
    print(n,'X',i,'=',i*n)

#Listas
       
#1

listaNumeros = []
       
print ('Informe os 5 numeros')
       
for i in range(5):
    listaNumero.append(input('Numero '+ str(i+1) + ':\n'))
       
print (listaNumeros) 
       
#2

listaNumerosReais = []
       
print ('Informe os 10 numeros reais')
       
for i in range(10):
    listaNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
       
listaNumerosReais.reverse()
       
print (listaNumerosReais) 

#3
       
listaNotas = []
media = 0
       
print ('Informe as 4 notas')
       
for i in range(4):
    listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))

soma = sum(listaNotas)
media = soma/4
       
print (listaNotas) 
print (media)
     
#4
       
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
       
#5
    
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
       
#6
       
listaNotas = []
notasAluno = []
       
print ('Notas dos Alunos')
for i in range(10):
    media = 0
    notasAluno = []
    print ('Aluno: ' + str(i + 1))
    for j in range(4):
        notasAluno.append(float(input('Nota: ' + str(j+1) + '\n')))
        media += notasAluno[j]
        print (media)
    media = media/4
    listaNotas.append(media)
       
#7
       
idades = []
alturas = []

for valor in range(0, 5):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))

print("Idades na ordem inversa: ")
for valor in range(0, 5):
    print(idades[len(idades)-1-valor])

print("Alturas na ordem inversa: ")
for valor in range(0, 5):
    print(alturas[len(alturas)-1-valor])
       
#8
       
vetorA = []
soma = 0
       
for numero in range(0, 10):
    vetorA.append(int(input("Digite um número: ")))
    soma = soma + (vetorA[len(vetorA)-1]**2)
       
print("A soma dos quadrados dos elementos do vetor são " + str(soma))
       
#9
       
import random

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
	lista1.append(random.randint(1,100))
	lista2.append(random.randint(1,100))
	lista3.append(lista1[i])
	lista3.append(lista2[i])

print lista1
print lista2
print lista3 




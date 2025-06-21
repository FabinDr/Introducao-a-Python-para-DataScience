#Coleta e amostragem de dados

#1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

nome = input("Escreva o seu nome: ");
print("Olá! %s " %(nome));

#resposta usando a formatação f-string

nome = input('Digite seu nome: ');
print(f'Olá, {nome}.');

#2. Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.

nome = input("Escreva o seu nome: ");
idade = int(input('Escreva a sua idade: '));
print("Olá! %s,  você tem %d anos" %(nome, idade));

#3. Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.

nome = input("Escreva o seu nome: ");
idade = int(input('Escreva a sua idade: '));
altura = float(input("Escreva a sua idade: "));

print("Olá! %s,  você tem %d anos e mede %f metros!" %(nome, idade));

#----------------------------------------
# Calculadora com operadores

# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.


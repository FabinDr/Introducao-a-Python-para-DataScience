#---------------Coleta e amostragem de dados--------------

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
# ------------- Calculadora com operadores -------------

#1. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
print("------------Soma dois números------------------")

n1 = int(input('Escreva um número inteiro: '));
n2 = int(input('Escreva outro número inteiro: '));

soma = n1 + n2;
print(f' A soma entre {n1} e {n2} é: {soma}');

#2. Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
print("------------Soma três números------------------")

n1 = int(input('Escreva um número inteiro: '));
n2 = int(input('Escreva outro número inteiro: '));
n3 = int(input('Escreva outro número inteiro: '));

soma = n1 + n2 + n3;
print(f' A soma entre {n1}, {n2} e {n3} é: {soma}');

#3. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.

print("------------subtração de dois números------------------")

n1 = int(input('Escreva um número inteiro: '));
n2 = int(input('Escreva outro número inteiro: '));

subtracao = n1 - n2;
print(f' A subtração entre {n1} e {n2} é: {subtracao}');

#4. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
print("------------multipliação de dois números------------------")

n1 = int(input('Escreva um número inteiro: '));
n2 = int(input('Escreva outro número inteiro: '));

mult = n1 * n2;
print(f' A multiplicação entre {n1} e {n2} é: {mult}');

#5. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

print("------------Divisão de dois números------------------")

n1 = int(input('Escreva o numerador: '));
n2 = int(input('Escreva o denominador (diferente de 0): '));

div = n1 / n2;
print(f' A divisão entre {n1} e {n2} é: {div}');

#6. Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

print("------------ Potência ------------------")

n1 = int(input('Escreva o operador: '));
n2 = int(input('Escreva a potência: '));

poten = n1 ** n2;
print(f' o resultado é: {poten}');

#7. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

print("------------Divisão de dois números------------------")

n1 = int(input('Escreva o numerador: '));
n2 = int(input('Escreva o denominador (diferente de 0): '));

div = n1 // n2;
print(f' A divisão entre {n1} e {n2} é: {div}');

#8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

print("------------Divisão de dois números------------------")

n1 = int(input('Escreva o numerador: '));
n2 = int(input('Escreva o denominador (diferente de 0): '));

resto = n1 % n2;
print(f'O resto da divisão entre {n1} e {n2} é: {resto}');

#9. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nA média das notas é: {media:.2f}")

#10. Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4);
print(f"A média é: {media_ponderada}");

# -------------- Editando textos ---------------
